"""Product GIF Maker

Takes a product photo, cuts the product off its background, and turns it into
an animated GIF where the product sways side to side while a speech bubble
shows the joke (or riddle) of the day.

Usage:
    python product_gif.py products/bisou_balm.png
    python product_gif.py products/bisou_balm.png --kind riddle
    python product_gif.py products/bisou_balm.png --text "Kiss boring lips goodbye!"
"""

import argparse
import math
import random
from datetime import date
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

from jokes import JOKES, RIDDLES

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


# ---------- picking today's joke / riddle ----------

def pick_of_the_day(kind, day):
    """Same date -> same pick, so everyone sees the same joke that day."""
    if kind == "auto":
        kind = "joke" if day.toordinal() % 2 == 0 else "riddle"
    pool = JOKES if kind == "joke" else RIDDLES
    question, answer = random.Random(day.toordinal()).choice(pool)
    return kind, question, answer


# ---------- cutting the product out ----------

def cut_out_product(image, tolerance=40):
    """Remove the flat background colour that touches the image edges."""
    rgb = image.convert("RGB")
    bg_color = rgb.getpixel((2, 2))

    # White where a pixel looks like the background, black elsewhere
    diff = ImageChops.difference(rgb, Image.new("RGB", rgb.size, bg_color))
    looks_like_bg = diff.convert("L").point(lambda v: 255 if v < tolerance else 0)

    # Flood fill from every corner so we only remove background that is
    # connected to the edge (keeps any yellow parts inside the product)
    w, h = looks_like_bg.size
    for corner in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        if looks_like_bg.getpixel(corner) == 255:
            ImageDraw.floodfill(looks_like_bg, corner, 128)

    alpha = looks_like_bg.point(lambda v: 0 if v == 128 else 255)
    alpha = alpha.filter(ImageFilter.GaussianBlur(1))

    product = image.convert("RGBA")
    product.putalpha(alpha)
    return product.crop(alpha.getbbox()), bg_color


# ---------- drawing the speech bubble ----------

def wrap_text(text, font, max_width, draw):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def draw_bubble(canvas, title, body, tail_x, tail_y, accent):
    draw = ImageDraw.Draw(canvas)
    W = canvas.width
    pad = int(W * 0.04)
    box_left, box_right = int(W * 0.08), int(W * 0.92)
    box_top = int(W * 0.06)

    title_font = ImageFont.truetype(FONT_BOLD, int(W * 0.035))
    body_font = ImageFont.truetype(FONT_REGULAR, int(W * 0.042))
    lines = wrap_text(body, body_font, box_right - box_left - 2 * pad, draw)
    line_h = int(body_font.size * 1.3)

    box_bottom = box_top + pad + title_font.size + int(pad * 0.6) + line_h * len(lines) + pad
    outline = (40, 40, 40)
    stroke = max(3, W // 180)

    # Tail: a triangle from the bubble's bottom edge down toward the product
    base_x = min(max(tail_x, box_left + 80), box_right - 80)
    tail = [(base_x - 30, box_bottom - stroke), (base_x + 30, box_bottom - stroke), (tail_x, tail_y)]

    draw.rounded_rectangle([box_left, box_top, box_right, box_bottom], radius=30,
                           fill="white", outline=outline, width=stroke)
    draw.polygon(tail, fill="white", outline=outline, width=stroke)
    # Cover the outline where the tail joins the bubble
    draw.line([(base_x - 30 + stroke, box_bottom - stroke), (base_x + 30 - stroke, box_bottom - stroke)],
              fill="white", width=stroke * 2)

    y = box_top + pad
    draw.text((box_left + pad, y), title, font=title_font, fill=accent)
    y += title_font.size + int(pad * 0.6)
    for line in lines:
        draw.text((box_left + pad, y), line, font=body_font, fill=outline)
        y += line_h
    return box_bottom


# ---------- building the GIF ----------

def make_gif(product_path, output_path, kind="auto", text=None, day=None,
             width=600, frames=48, frame_ms=70, sway=0.08, tilt=5):
    day = day or date.today()
    source = Image.open(product_path)
    product, bg_color = cut_out_product(source)

    # Output canvas keeps the source's aspect ratio
    height = int(width * source.height / source.width)
    scale = (height * 0.62) / product.height
    product = product.resize((int(product.width * scale), int(product.height * scale)), Image.LANCZOS)

    if text:
        kind, question, answer = "custom", text, None
        title = "PSST..."
    else:
        kind, question, answer = pick_of_the_day(kind, day)
        title = f"{kind.upper()} OF THE DAY  ·  {day:%b %d}"

    accent = (200, 60, 110)
    frame_list = []
    for i in range(frames):
        t = i / frames
        # Two full side-to-side swings per loop
        wave = math.sin(2 * math.pi * 2 * t)
        offset_x = int(wave * width * sway)
        angle = -wave * tilt

        canvas = Image.new("RGB", (width, height), bg_color)
        rotated = product.rotate(angle, resample=Image.BICUBIC, expand=True)
        x = (width - rotated.width) // 2 + offset_x
        y = height - rotated.height - int(height * 0.04)
        canvas.paste(rotated, (x, y), rotated)

        # Riddles show the question first, then reveal the answer
        if answer and t >= 0.5:
            body = f"{question}  →  {answer}" if kind == "joke" else f"Answer: {answer}"
        else:
            body = question
        draw_bubble(canvas, title, body, tail_x=width // 2 + offset_x,
                    tail_y=y + int(rotated.height * 0.05), accent=accent)
        frame_list.append(canvas)

    # One shared palette for every frame keeps the file small and flicker-free
    palette = frame_list[0].quantize(colors=128, method=Image.MEDIANCUT)
    frame_list = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frame_list]

    frame_list[0].save(output_path, save_all=True, append_images=frame_list[1:],
                       duration=frame_ms, loop=0, optimize=True)
    return question, answer


def main():
    parser = argparse.ArgumentParser(description="Turn a product photo into a swaying GIF with a joke bubble.")
    parser.add_argument("image", help="path to the product photo")
    parser.add_argument("-o", "--output", help="output GIF path (default: <image>_<date>.gif)")
    parser.add_argument("--kind", choices=["auto", "joke", "riddle"], default="auto",
                        help="auto alternates jokes and riddles by day")
    parser.add_argument("--text", help="use your own bubble text instead of the joke of the day")
    parser.add_argument("--date", type=date.fromisoformat, help="pick the joke for this date (YYYY-MM-DD)")
    parser.add_argument("--width", type=int, default=600, help="GIF width in pixels")
    args = parser.parse_args()

    day = args.date or date.today()
    output = args.output or str(Path(args.image).with_name(f"{Path(args.image).stem}_{day}.gif"))
    question, answer = make_gif(args.image, output, kind=args.kind, text=args.text, day=day, width=args.width)
    print(f"Bubble: {question}" + (f"  ->  {answer}" if answer else ""))
    print(f"Saved GIF to {output}")


if __name__ == "__main__":
    main()
