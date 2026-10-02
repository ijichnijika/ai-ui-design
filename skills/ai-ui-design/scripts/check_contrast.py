#!/usr/bin/env python3
"""Compute WCAG 2.x contrast ratios for foreground/background color pairs."""

from __future__ import annotations

import argparse
import math
import re
import sys


HEX = re.compile(r"^#?([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
FUNCTION = re.compile(r"^(rgba?|oklch)\((.*)\)$", re.I)
TOKEN = re.compile(r"[a-zA-Z]+\([^)]*\)|[^\s,/]+")
THRESHOLDS = {"text": 4.5, "large": 3.0}
FORMATS = "#rgb、#rgba、#rrggbb、#rrggbbaa、rgb() 或 oklch()"


def number(token: str, scale: float) -> float:
    """Percentages are fractions of scale; `none` counts as zero."""
    if token.lower() == "none":
        return 0.0
    return float(token[:-1]) / 100 * scale if token.endswith("%") else float(token)


def encode(linear: float) -> float:
    linear = min(max(linear, 0.0), 1.0)
    return linear * 12.92 if linear <= 0.0031308 else 1.055 * linear ** (1 / 2.4) - 0.055


def oklch_to_srgb(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    """OKLCH to gamma-encoded sRGB; out-of-gamut channels are clipped."""
    a, b = chroma * math.cos(math.radians(hue)), chroma * math.sin(math.radians(hue))
    l = (lightness + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (lightness - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (lightness - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (encode(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
            encode(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
            encode(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s))


def parse_color(value: str) -> tuple[float, float, float, float]:
    """Return gamma-encoded sRGB channels and alpha, each in 0–1."""
    text = value.strip()
    match = HEX.match(text)
    if match:
        digits = match.group(1)
        if len(digits) in (3, 4):
            digits = "".join(c * 2 for c in digits)
        channels = [int(digits[i:i + 2], 16) / 255 for i in range(0, len(digits), 2)]
        return (*channels[:3], channels[3] if len(channels) == 4 else 1.0)
    match = FUNCTION.match(text)
    parts = re.split(r"[\s,/]+", match.group(2).strip()) if match else []
    if len(parts) not in (3, 4):
        raise ValueError(f"无法解析色值 {value!r}：需要 {FORMATS}")
    try:
        alpha = number(parts[3], 1) if len(parts) == 4 else 1.0
        if match.group(1).lower() == "oklch":
            rgb = oklch_to_srgb(number(parts[0], 1), number(parts[1], 0.4), number(re.sub(r"deg$", "", parts[2]), 360))
        else:
            rgb = tuple(min(max(number(p, 255) / 255, 0.0), 1.0) for p in parts[:3])
    except ValueError:
        raise ValueError(f"无法解析色值 {value!r}：需要 {FORMATS}") from None
    return (*rgb, min(max(alpha, 0.0), 1.0))


def luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    *back, back_alpha = parse_color(bg)
    if back_alpha < 1:
        raise ValueError(f"背景 {bg!r} 带透明度：换成它在页面上实际呈现的不透明色")
    *front, alpha = parse_color(fg)
    shown = tuple(alpha * f + (1 - alpha) * b for f, b in zip(front, back))
    a, b = sorted((luminance(shown), luminance(tuple(back))), reverse=True)
    return (a + 0.05) / (b + 0.05)


def parse_pair(value: str, default_level: str) -> tuple[str, str, str]:
    parts = TOKEN.findall(value)
    level = default_level
    if len(parts) == 3 and parts[2] in THRESHOLDS:
        level = parts.pop()
    if len(parts) != 2:
        raise ValueError(f"{value!r} 需要 \"<前景> <背景> [text|large]\"")
    return parts[0], parts[1], level


def main() -> int:
    parser = argparse.ArgumentParser(description="计算前景/背景色对的 WCAG 对比度；半透明前景先按背景合成再算")
    parser.add_argument("pairs", nargs="+", help=f'色对，如 "#161616 #f4f4f4"；末尾可加 text 或 large 单独指定门槛。色值支持 {FORMATS}')
    parser.add_argument(
        "--level",
        choices=sorted(THRESHOLDS),
        default="text",
        help="未单独指定的色对使用的门槛：text 为正文 4.5:1，large 为大字与 UI 组件 3:1（默认 text）",
    )
    args = parser.parse_args()

    rows = []
    for raw in args.pairs:
        try:
            fg, bg, level = parse_pair(raw, args.level)
            rows.append((fg, bg, level, contrast(fg, bg)))
        except ValueError as exc:
            print(f"错误：{exc}", file=sys.stderr)
            return 2

    width = max(9, *(len(color) for fg, bg, _, _ in rows for color in (fg, bg)))
    failed = 0
    print(f"{'前景':<{width}} {'背景':<{width}} {'对比度':>7}  {'门槛':<5}  结果")
    for fg, bg, level, ratio in rows:
        ok = ratio >= THRESHOLDS[level]
        print(f"{fg:<{width}} {bg:<{width}} {ratio:>6.2f}:1  {level:<5}  {'达标' if ok else '不达标'}（需 {THRESHOLDS[level]}:1）")
        failed += not ok
    if failed:
        print(f"{failed} 对不达标", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
