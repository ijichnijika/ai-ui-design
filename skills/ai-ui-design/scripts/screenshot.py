#!/usr/bin/env python3
"""Screenshot pages with an installed Chromium-family browser over CDP, using only the standard library."""

from __future__ import annotations

import argparse
import base64
import glob
import json
import os
from pathlib import Path
import re
import select
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1]
PRESETS = {"desktop": (1440, 900, 1.0, False), "mobile": (390, 844, 2.0, True)}
KEYS = {"Tab": 9, "Enter": 13, "Escape": 27, "Space": 32, "ArrowLeft": 37, "ArrowUp": 38, "ArrowRight": 39, "ArrowDown": 40}
FLAGS = [
    "--headless=new", "--remote-debugging-port=0", "--no-first-run", "--no-default-browser-check",
    "--disable-extensions", "--disable-sync", "--disable-default-apps", "--disable-component-update",
    "--disable-background-networking", "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows", "--disable-renderer-backgrounding", "--disable-dev-shm-usage",
    "--password-store=basic", "--use-mock-keychain", "--force-color-profile=srgb", "--hide-scrollbars",
    "--mute-audio", "--disable-breakpad", "--disable-features=Translate,MediaRouter,OptimizationHints",
]

# The measurable items of build-and-verify.md, reported with every screenshot.
CHECKS = r"""(() => {
  if (!document.body) return {blank: true};
  // The layout viewport: mobile emulation widens innerWidth to fit overflowing content.
  const vw = document.documentElement.clientWidth;
  const label = el => {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    else if (typeof el.className === 'string' && el.className.trim()) s += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
    const text = (el.innerText || el.getAttribute('aria-label') || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 24);
    return text ? `${s} "${text}"` : s;
  };
  const shown = el => {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && +cs.opacity > 0;
  };
  const all = [...document.body.querySelectorAll('*')];
  const overflowX = Math.max(0, document.documentElement.scrollWidth - vw);
  const wide = overflowX ? all.filter(el => el.getBoundingClientRect().right > vw + 1
    && el.parentElement.getBoundingClientRect().right <= vw + 1 && shown(el)).map(label) : [];
  const tiny = all.filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && shown(el))
    .map(el => [el, parseFloat(getComputedStyle(el).fontSize)]).filter(([, size]) => size < 12)
    .map(([el, size]) => `${label(el)} ${size}px`);
  const hits = [...document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=checkbox], [role=switch], [role=tab], [tabindex]:not([tabindex="-1"])')]
    .filter(el => shown(el) && getComputedStyle(el).display !== 'inline')
    .map(el => [el, el.getBoundingClientRect()]).filter(([, r]) => r.width < 24 || r.height < 24)
    .map(([el, r]) => `${label(el)} ${Math.round(r.width)}×${Math.round(r.height)}`);
  const blank = !document.body.innerText.trim() && !document.querySelector('img, svg, canvas, video, iframe, picture');
  return {overflowX, overflowBy: wide.slice(0, 3), smallText: tiny.length, smallTextSamples: tiny.slice(0, 3),
          smallTargets: hits.length, smallTargetSamples: hits.slice(0, 3), blank};
})()"""

# Before actions: settle what is already moving, and remember it so frames show only what the actions start.
MARK = r"""(() => {
  const list = document.getAnimations();
  for (const a of list) { try { a.finish(); } catch (e) {} }
  window.__aiuiBefore = new Set(list);
})()"""

# Pause the animations at one shared moment of the longest, so staggered choreography stays intact.
SEEK = r"""(fraction => {
  const before = window.__aiuiBefore || new Set();
  const list = document.getAnimations().filter(a => !before.has(a));
  const timing = list.map(a => a.effect ? a.effect.getComputedTiming() : {});
  const ends = timing.map(t => t.endTime).filter(Number.isFinite);
  const span = ends.length ? Math.max(...ends) : Math.max(0, ...timing.map(t => (t.delay || 0) + (Number(t.duration) || 0)));
  for (const a of list) { a.pause(); a.currentTime = span * fraction; }
  return list.length;
})"""


def find_browser(explicit: str | None) -> str:
    """An explicit path, then installed browsers, then copies cached by Playwright or Puppeteer."""
    if explicit:
        if Path(explicit).is_file():
            return explicit
        raise LookupError(f"找不到指定的浏览器：{explicit}")
    home = Path.home()
    if sys.platform == "darwin":
        apps = ["Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser", "Google Chrome Canary"]
        installed = [str(root / f"{app}.app/Contents/MacOS/{app}") for root in (Path("/Applications"), home / "Applications") for app in apps]
        caches, names = [home / "Library/Caches/ms-playwright", home / ".cache/puppeteer"], ["*.app/Contents/MacOS/*", "chrome-headless-shell", "headless_shell"]
    elif os.name == "nt":
        roots = [os.environ.get(key, "") for key in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA")]
        apps = ["Google/Chrome/Application/chrome.exe", "Microsoft/Edge/Application/msedge.exe",
                "Chromium/Application/chrome.exe", "BraveSoftware/Brave-Browser/Application/brave.exe"]
        installed = [str(Path(root) / app) for root in roots if root for app in apps]
        caches, names = [Path(os.environ.get("LOCALAPPDATA", home)) / "ms-playwright", home / ".cache/puppeteer"], ["chrome.exe", "chrome-headless-shell.exe", "headless_shell.exe"]
    else:
        commands = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "microsoft-edge-stable", "brave-browser"]
        installed = [path for path in map(shutil.which, commands) if path]
        caches, names = [home / ".cache/ms-playwright", home / ".cache/puppeteer"], ["chrome", "chrome-headless-shell", "headless_shell"]
    cached = [hit for cache in caches for depth in ("chrom*/*", "chrom*/*/*") for name in names
              for hit in sorted(glob.glob(str(cache / depth / name)), reverse=True)]
    for candidate in installed + cached:
        if Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return candidate
    raise LookupError("没找到 Chrome、Edge、Chromium 或 Brave；用 --browser 或环境变量 CHROME_PATH 指定可执行文件")


class Browser:
    """A headless browser process, driven over a minimal RFC 6455 WebSocket client speaking CDP."""

    def __init__(self, binary: str, timeout: float, cache: Path):
        self.timeout, self.listeners, self.next_id = timeout, [], 0
        self.buffer, self.partial, self.sock = bytearray(), bytearray(), None
        self.profile = tempfile.mkdtemp(prefix="chrome-", dir=cache)
        flags = FLAGS + [f"--user-data-dir={self.profile}"]
        if hasattr(os, "geteuid") and os.geteuid() == 0:
            flags.append("--no-sandbox")
        self.process = subprocess.Popen([binary, *flags, "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            self._connect(self._endpoint())
        except BaseException:
            self.close()
            raise

    def _endpoint(self) -> str:
        marker, deadline = Path(self.profile) / "DevToolsActivePort", time.monotonic() + 20
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f"浏览器启动后立刻退出了（退出码 {self.process.returncode}）")
            try:
                lines = marker.read_text().split("\n")
            except OSError:
                lines = []
            if len(lines) > 1 and lines[0].strip().isdigit() and lines[1].strip():
                return f"ws://127.0.0.1:{lines[0].strip()}{lines[1].strip()}"
            time.sleep(0.05)
        raise RuntimeError("浏览器 20 秒内没有打开调试端口")

    def _connect(self, url: str) -> None:
        parts = urlsplit(url)
        self.sock = socket.create_connection((parts.hostname, parts.port), timeout=self.timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET {parts.path} HTTP/1.1\r\nHost: {parts.hostname}:{parts.port}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        while b"\r\n\r\n" not in self.buffer:
            self._fill()
        end = self.buffer.index(b"\r\n\r\n") + 4
        status = bytes(self.buffer[:end]).split(b"\r\n", 1)[0].decode("latin-1")
        del self.buffer[:end]
        if status.split()[1:2] != ["101"]:
            raise RuntimeError(f"浏览器拒绝了调试连接：{status}")

    def _fill(self) -> None:
        chunk = self.sock.recv(1 << 20)
        if not chunk:
            raise RuntimeError("浏览器断开了调试连接")
        self.buffer.extend(chunk)

    def _frame_length(self) -> int:
        """Bytes of the first frame once it has fully arrived, else 0."""
        buf = self.buffer
        if len(buf) < 2:
            return 0
        size, start = buf[1] & 0x7F, 2
        if size > 125:
            start = 4 if size == 126 else 10
            if len(buf) < start:
                return 0
            size = int.from_bytes(buf[2:start], "big")
        total = start + (4 if buf[1] & 0x80 else 0) + size
        return total if len(buf) >= total else 0

    def _read(self) -> dict | None:
        """Block for one frame and return the message it completes, if any."""
        while not (total := self._frame_length()):
            self._fill()
        frame = bytes(self.buffer[:total])
        del self.buffer[:total]
        payload = frame[{126: 4, 127: 10}.get(frame[1] & 0x7F, 2):]
        if frame[1] & 0x80:
            payload = self._mask(payload[4:], payload[:4])
        opcode = frame[0] & 0x0F
        if opcode == 0x8:
            raise RuntimeError("浏览器关闭了调试连接")
        if opcode == 0x9:
            self._write(0xA, payload)
        elif opcode in (0x0, 0x1, 0x2):
            self.partial.extend(payload)
            if frame[0] & 0x80:
                message = json.loads(bytes(self.partial))
                self.partial.clear()
                return message
        return None

    def _write(self, opcode: int, payload: bytes) -> None:
        size = len(payload)
        if size < 126:
            length = bytes([0x80 | size])
        elif size < 1 << 16:
            length = bytes([0x80 | 126]) + size.to_bytes(2, "big")
        else:
            length = bytes([0x80 | 127]) + size.to_bytes(8, "big")
        key = os.urandom(4)
        self.sock.sendall(bytes([0x80 | opcode]) + length + key + self._mask(payload, key))

    @staticmethod
    def _mask(data: bytes, key: bytes) -> bytes:
        stream = (key * (len(data) // 4 + 1))[:len(data)]
        return (int.from_bytes(data, "big") ^ int.from_bytes(stream, "big")).to_bytes(len(data), "big")

    def send(self, method: str, params: dict | None = None, session: str | None = None) -> dict:
        self.next_id += 1
        request = {"id": self.next_id, "method": method, "params": params or {}}
        if session:
            request["sessionId"] = session
        self._write(0x1, json.dumps(request).encode())
        while True:
            message = self._read()
            if message is None:
                continue
            if message.get("id") == self.next_id:
                if "error" in message:
                    raise RuntimeError(f"{method}：{message['error'].get('message')}")
                return message.get("result", {})
            self._dispatch(message)

    def pump(self, seconds: float) -> None:
        """Keep dispatching events while waiting."""
        deadline = time.monotonic() + seconds
        while (left := deadline - time.monotonic()) > 0:
            if self._frame_length() or select.select([self.sock], [], [], left)[0]:
                message = self._read()
                if message:
                    self._dispatch(message)

    def _dispatch(self, message: dict) -> None:
        for listener in self.listeners:
            listener(message)

    def evaluate(self, expression: str, session: str):
        result = self.send("Runtime.evaluate", {"expression": expression, "awaitPromise": True, "returnByValue": True}, session)
        if "exceptionDetails" in result:
            details = result["exceptionDetails"]
            raise RuntimeError(f"页面脚本出错：{(details.get('exception') or {}).get('description') or details.get('text')}")
        return result.get("result", {}).get("value")

    def close(self) -> None:
        if self.sock:
            try:
                self.send("Browser.close")
            except (OSError, RuntimeError):
                pass
            self.sock.close()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()
        for _ in range(10):  # Windows keeps files locked until helper processes exit
            shutil.rmtree(self.profile, ignore_errors=True)
            if not os.path.exists(self.profile):
                break
            time.sleep(0.3)


def cache_dir(out: Path) -> Path:
    """`.cache/ai-ui-design` of the project holding the screenshots; the system temp folder when it is read-only."""
    root = next((folder for folder in (out, *out.parents) if (folder / ".git").exists() or (folder / "package.json").exists()), out)
    cache = root / ".cache" / "ai-ui-design"
    try:
        cache.mkdir(parents=True, exist_ok=True)
        (cache / ".gitignore").write_text("*\n")
        os.rmdir(tempfile.mkdtemp(dir=cache))  # entries must be creatable, not just the folder present
    except OSError:
        cache = Path(tempfile.gettempdir()) / "ai-ui-design"
        cache.mkdir(exist_ok=True)
    return cache


def in_use(profile: Path) -> bool:
    """Whether a live run still owns this profile: its browser answers, or it is under an hour old and starting up."""
    try:
        port = int((profile / "DevToolsActivePort").read_text().split("\n")[0])
    except (OSError, ValueError):
        try:
            return time.time() - profile.stat().st_mtime < 3600
        except OSError:
            return False
    try:
        socket.create_connection(("127.0.0.1", port), timeout=0.2).close()
        return True
    except OSError:
        return False


def sweep(cache: Path) -> None:
    """Delete profiles left behind by runs that were killed."""
    for profile in cache.glob("chrome-*"):
        if not in_use(profile):
            shutil.rmtree(profile, ignore_errors=True)


class Page:
    """Load state and problems of one tab, collected from its CDP events."""

    def __init__(self, session: str):
        self.session, self.frame, self.loaded, self.status = session, None, False, None
        self.inflight, self.urls, self.problems, self.last_network = set(), {}, [], time.monotonic()

    def __call__(self, message: dict) -> None:
        if message.get("sessionId") != self.session:
            return
        method, params = message.get("method", ""), message.get("params", {})
        if method.startswith("Network."):
            self.last_network = time.monotonic()
        if method == "Page.loadEventFired":
            self.loaded = True
        elif method == "Network.requestWillBeSent":
            self.inflight.add(params["requestId"])
            self.urls[params["requestId"]] = params["request"]["url"]
        elif method in ("Network.loadingFinished", "Network.loadingFailed"):
            self.inflight.discard(params["requestId"])
            if method == "Network.loadingFailed" and not params.get("canceled"):
                self.note(f"请求失败 {params.get('errorText')}：{self.urls.get(params['requestId'], '')}")
        elif method == "Network.responseReceived":
            status, url = params["response"].get("status", 0), params["response"].get("url", "")
            if params.get("type") == "Document" and params.get("frameId") == self.frame and self.status is None:
                self.status = status
            if status >= 400 and not url.endswith("/favicon.ico"):
                self.note(f"HTTP {status}：{url}")
        elif method == "Runtime.exceptionThrown":
            details = params.get("exceptionDetails", {})
            self.note("脚本异常：" + ((details.get("exception") or {}).get("description") or details.get("text", "")).split("\n")[0])
        elif method == "Runtime.consoleAPICalled" and params.get("type") == "error":
            self.note("console.error：" + " ".join(str(arg.get("value", arg.get("description", ""))) for arg in params.get("args", [])))

    def note(self, text: str) -> None:
        text = text[:240]
        if text not in self.problems:
            self.problems.append(text)


def act(browser: Browser, session: str, action: str, deadline: float, settle: bool) -> None:
    kind, _, value = action.partition(":")
    find = f"document.querySelector({json.dumps(value.split('=>')[0])})"
    if kind == "wait":
        if re.fullmatch(r"\d+(\.\d+)?", value):
            browser.pump(float(value) / 1000)
            return
        while not browser.evaluate(f"!!{find}", session):
            if time.monotonic() > deadline:
                raise RuntimeError(f"等不到元素 {value}")
            browser.pump(0.1)
        return
    if kind in ("click", "hover"):
        point = browser.evaluate(f"(el => {{ if (!el) return null; el.scrollIntoView({{block: 'center', inline: 'center'}});"
                                 f" const r = el.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; }})({find})", session)
        if point is None:
            raise RuntimeError(f"找不到元素 {value}")
        mouse = {"x": point[0], "y": point[1]}
        browser.send("Input.dispatchMouseEvent", {"type": "mouseMoved", **mouse}, session)
        if kind == "click":
            for phase in ("mousePressed", "mouseReleased"):
                browser.send("Input.dispatchMouseEvent", {"type": phase, "button": "left", "clickCount": 1, **mouse}, session)
    elif kind in ("focus", "type"):
        selector, _, text = value.partition("=>")
        if not browser.evaluate(f"(el => {{ el?.focus(); return !!el; }})({find})", session):
            raise RuntimeError(f"找不到元素 {selector}")
        if text:
            browser.send("Input.insertText", {"text": text}, session)
    elif kind == "press":
        key, _, times = value.partition("*")
        if key not in KEYS:
            raise ValueError(f"不支持的按键 {key}；可用 {'、'.join(KEYS)}")
        text = {"Enter": "\r", "Space": " "}.get(key)
        for _ in range(int(times or 1)):
            for phase in ("keyDown" if text else "rawKeyDown", "keyUp"):
                event = {"type": phase, "key": " " if key == "Space" else key, "code": key, "windowsVirtualKeyCode": KEYS[key]}
                if text and phase == "keyDown":
                    event["text"] = text
                browser.send("Input.dispatchKeyEvent", event, session)
    elif kind == "scroll":
        browser.evaluate(f"scrollTo(0, {value})" if re.fullmatch(r"\d+(\.\d+)?", value) else f"{find}?.scrollIntoView({{block: 'start'}})", session)
    elif kind == "eval":
        browser.evaluate(value, session)
    else:
        raise ValueError(f"不认识的动作 {action}；可用 click、hover、focus、type、press、scroll、wait、eval")
    if settle:
        browser.pump(0.2)


def shoot(browser: Browser, session: str, path: Path, viewport: tuple, full: bool, page: Page) -> str:
    width, _, scale, _ = viewport
    params: dict = {"format": "png"}
    if full:
        metrics = browser.send("Page.getLayoutMetrics", session=session)
        height, limit = (metrics.get("cssContentSize") or metrics["contentSize"])["height"], 16384 / scale
        if height > limit:
            page.note(f"页面高 {height:.0f}px，整页截图只截到前 {limit:.0f}px")
        params.update(captureBeyondViewport=True, clip={"x": 0, "y": 0, "width": width, "height": min(height, limit), "scale": 1})
    path.write_bytes(base64.b64decode(browser.send("Page.captureScreenshot", params, session)["data"]))
    return str(path)


def capture(browser: Browser, target: str, viewport: tuple, args: argparse.Namespace, out: Path) -> dict:
    width, height, scale, mobile = viewport
    tab = browser.send("Target.createTarget", {"url": "about:blank"})["targetId"]
    session = browser.send("Target.attachToTarget", {"targetId": tab, "flatten": True})["sessionId"]
    page = Page(session)
    browser.listeners.append(page)
    try:
        for domain in ("Page", "Runtime", "Network"):
            browser.send(f"{domain}.enable", session=session)
        page.frame = browser.send("Page.getFrameTree", session=session)["frameTree"]["frame"]["id"]
        browser.send("Emulation.setDeviceMetricsOverride", {"width": width, "height": height, "deviceScaleFactor": scale, "mobile": mobile}, session)
        browser.send("Emulation.setFocusEmulationEnabled", {"enabled": True}, session)
        if mobile:
            browser.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5}, session)
        media = [{"name": "prefers-reduced-motion", "value": "reduce"}] if args.reduced_motion else []
        if args.dark:
            media.append({"name": "prefers-color-scheme", "value": "dark"})
        if media:
            browser.send("Emulation.setEmulatedMedia", {"features": media}, session)
        if args.frames:
            # Slow the timeline so animations are still running when the frames are taken.
            browser.send("Animation.enable", session=session)
            browser.send("Animation.setPlaybackRate", {"playbackRate": 0.01}, session)
        error = browser.send("Page.navigate", {"url": target}, session).get("errorText")
        if error:
            raise RuntimeError(f"打不开 {target}：{error}")
        deadline = time.monotonic() + args.timeout
        while not page.loaded and time.monotonic() < deadline:
            browser.pump(0.1)
        if not page.loaded:
            page.note(f"{args.timeout:g} 秒内没等到 load 事件，截到的可能是加载中的画面")
        quiet_until = min(deadline, time.monotonic() + 8)
        while time.monotonic() < quiet_until and (page.inflight or time.monotonic() - page.last_network < 0.5):
            browser.pump(0.1)
        browser.evaluate("document.fonts.ready.then(() => true)", session)
        browser.pump(args.wait / 1000)
        if args.frames and args.do:
            browser.evaluate(MARK, session)
        for action in args.do:
            act(browser, session, action, deadline, settle=not args.frames)
        report = browser.evaluate(CHECKS, session) or {}
        name = shot_name(target, args.name, viewport)
        if args.frames:
            files, count = [], 0
            for index in range(args.frames):
                fraction = index / (args.frames - 1) if args.frames > 1 else 1.0
                count = browser.evaluate(f"{SEEK}({fraction})", session)
                files.append(shoot(browser, session, out / f"{name}-f{round(fraction * 100)}.png", viewport, args.full, page))
            if not count:
                page.note("没有可暂停的 CSS/WAAPI 动画；JS 逐帧驱动的动画请改用录屏")
        else:
            files = [shoot(browser, session, out / f"{name}.png", viewport, args.full, page)]
        return {"target": target, "viewport": viewport_label(viewport), "files": files, "title": browser.evaluate("document.title", session),
                "status": page.status, "problems": page.problems, **report}
    finally:
        browser.listeners.remove(page)
        try:
            browser.send("Target.closeTarget", {"targetId": tab})
        except (OSError, RuntimeError):
            pass


def viewport_label(viewport: tuple) -> str:
    width, height, scale, mobile = viewport
    return ("mobile-" if mobile else "") + f"{width}x{height}" + (f"@{scale:g}" if scale != 1 else "")


def shot_name(target: str, label: str | None, viewport: tuple) -> str:
    parts = urlsplit(target)
    base = Path(parts.path).stem if parts.scheme == "file" else " ".join(filter(None, [parts.hostname, str(parts.port or ""), parts.path, parts.query]))
    slug = lambda text: re.sub(r"[^\w]+", "-", text.lower()).strip("-_")
    return "-".join(filter(None, [slug(base) or "page", slug(label or ""), viewport_label(viewport)]))


def normalize(target: str) -> str:
    if Path(target).exists():
        return Path(target).resolve().as_uri()
    if re.match(r"(localhost|127\.0\.0\.1|\[::1\])(:\d+)?(/|$)", target):
        return "http://" + target
    if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*://|about:|data:", target):
        return target
    raise ValueError(f"{target} 既不是 URL，也不是存在的文件")


def parse_viewport(spec: str) -> tuple:
    if spec in PRESETS:
        return PRESETS[spec]
    match = re.fullmatch(r"(mobile:)?(\d+)x(\d+)(?:@(\d+(?:\.\d+)?))?", spec)
    if not match:
        raise argparse.ArgumentTypeError(f"视口写成 desktop、mobile、1280x800 或 mobile:375x667@3：{spec}")
    return int(match[2]), int(match[3]), float(match[4] or 1), bool(match[1])


def main() -> int:
    if sys.version_info < (3, 9):
        print("需要 Python 3.9 或更新版本", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description="用本机已装的 Chrome、Edge、Chromium 或 Brave 无头截图并做基础检查；只用 Python 标准库")
    parser.add_argument("targets", nargs="+", help="URL（如 http://localhost:5173/orders）或本地 HTML 文件")
    parser.add_argument("--out", type=Path, required=True, help="截图目录，放在任务目录下")
    parser.add_argument("--viewport", action="append", type=parse_viewport,
                        help="desktop（1440x900）、mobile（390x844@2，触屏）、WxH[@DPR] 或 mobile:WxH[@DPR]；可重复，默认桌面加手机")
    parser.add_argument("--full", action="store_true", help="截整页，看长页节奏；默认只截首屏")
    parser.add_argument("--do", action="append", default=[], metavar="ACTION",
                        help="截图前依次执行：click:SEL、hover:SEL、focus:SEL、type:SEL=>文本、press:Tab*3、scroll:SEL或像素、wait:毫秒或SEL、eval:JS")
    parser.add_argument("--name", help="写进文件名的状态，如 hover、error")
    parser.add_argument("--frames", type=int, default=0, help="把动画暂停在 N 个均匀时刻各截一张；起、中、止用 3")
    parser.add_argument("--reduced-motion", action="store_true", help="模拟 prefers-reduced-motion: reduce")
    parser.add_argument("--dark", action="store_true", help="模拟 prefers-color-scheme: dark")
    parser.add_argument("--wait", type=float, default=300, help="网络空闲后再等的毫秒数（默认 300）")
    parser.add_argument("--timeout", type=float, default=30, help="单页超时秒数（默认 30）")
    parser.add_argument("--browser", default=os.environ.get("CHROME_PATH"), help="浏览器可执行文件；默认自动查找，也读 CHROME_PATH")
    args = parser.parse_args()
    out = args.out.resolve()
    if out.is_relative_to(SKILL_ROOT):
        print("未截图：截图不能写进 Skill 安装目录", file=sys.stderr)
        return 2
    try:
        targets = [normalize(target) for target in args.targets]
        binary = find_browser(args.browser)
    except (ValueError, LookupError) as exc:
        print(f"未截图：{exc}", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    for name in ("SIGTERM", "SIGHUP"):  # turn termination into SystemExit so the browser and profile get cleaned up
        if hasattr(signal, name):
            signal.signal(getattr(signal, name), lambda *_: sys.exit(1))
    shots, browser = [], None
    try:
        cache = cache_dir(out)
        sweep(cache)
        browser = Browser(binary, args.timeout, cache)
        for target in targets:
            for viewport in args.viewport or [PRESETS["desktop"], PRESETS["mobile"]]:
                try:
                    shots.append(capture(browser, target, viewport, args, out))
                except (RuntimeError, ValueError) as exc:
                    shots.append({"target": target, "viewport": viewport_label(viewport), "error": str(exc)})
    except (RuntimeError, OSError) as exc:
        shots.append({"error": f"浏览器出错：{exc}"})
    finally:
        if browser:
            browser.close()
    print(json.dumps({"browser": binary, "shots": shots}, ensure_ascii=False, indent=1))
    return 1 if any("error" in shot for shot in shots) else 0


if __name__ == "__main__":
    raise SystemExit(main())
