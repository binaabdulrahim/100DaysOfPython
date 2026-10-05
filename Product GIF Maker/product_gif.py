"""Product GIF Maker

Takes a product photo, cuts the product off its background, and turns it into
an MP4 video (or GIF) where the product sways side to side while a speech bubble
shows the joke (or riddle) of the day.

Usage:
    python product_gif.py products/bisou_balm.png          # MP4 (postable)
    python product_gif.py products/bisou_balm.png --gif    # GIF
    python product_gif.py products/bisou_balm.png --kind riddle
    python product_gif.py products/bisou_balm.png --text "Kiss boring lips goodbye!"
"""

import argparse
import math
import random
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

from jokes import JOKES, RIDDLES

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Output sizes for social apps: (width, height, top, bottom, right safe zones as fractions).
# The safe zones keep the bubble and product clear of each app's buttons and captions
# (TikTok / Reels put the like-comment-share column on the right, captions at the bottom).
SIZES = {
    "reels": (1080, 1920, 0.12, 0.22, 0.13),   # TikTok + Instagram Reels / Stories (9:16)
    "feed": (1080, 1350, 0.04, 0.04, 0.0),     # Instagram feed post (4:5)
    "square": (1080, 1080, 0.04, 0.04, 0.0),   # 1:1
}


# ---------- picking today's joke / riddle ----------

def pick_of_the_day(kind, day, index=0):
    """Same date -> same picks. `index` gives each product posted that day a different one."""
    if kind == "auto":
        kind = "joke" if day.toordinal() % 2 == 0 else "riddle"
    pool = list(JOKES if kind == "joke" else RIDDLES)
    random.Random(day.toordinal()).shuffle(pool)
    question, answer = pool[index % len(pool)]
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


def bubble_layout(canvas, body, box_top, safe_right=0.0):
    """Fonts, wrapped lines and the bubble's bottom edge for this text."""
    draw = ImageDraw.Draw(canvas)
    W = canvas.width
    pad = int(W * 0.04)
    box_left = int(W * (0.06 if safe_right else 0.08))
    box_right = int(W * (1 - safe_right - 0.02)) if safe_right else int(W * 0.92)
    title_font = ImageFont.truetype(FONT_BOLD, int(W * 0.035))
    body_font = ImageFont.truetype(FONT_REGULAR, int(W * 0.042))
    lines = wrap_text(body, body_font, box_right - box_left - 2 * pad, draw)
    line_h = int(body_font.size * 1.3)
    box_bottom = box_top + pad + title_font.size + int(pad * 0.6) + line_h * len(lines) + pad
    return draw, pad, box_left, box_right, title_font, body_font, lines, line_h, box_bottom


def draw_bubble(canvas, title, body, tail_x, tail_y, accent, box_top, safe_right=0.0):
    draw, pad, box_left, box_right, title_font, body_font, lines, line_h, box_bottom = \
        bubble_layout(canvas, body, box_top, safe_right)
    outline = (40, 40, 40)
    stroke = max(3, canvas.width // 180)

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


# ---------- building the animation ----------

def bubble_texts(kind, question, answer):
    """The bubble shows the question first, then the punchline / answer."""
    if not answer:
        return question, question
    return question, (f"{question}  →  {answer}" if kind == "joke" else f"Answer: {answer}")


def make_frames(product_path, kind="auto", text=None, day=None, size="reels", width=1080, frames=96,
                sway=0.08, tilt=5, index=0):
    """Return one loop of RGB frames (two side-to-side swings) plus the bubble text."""
    day = day or date.today()
    source = Image.open(product_path)
    product, bg_color = cut_out_product(source)

    if text:
        kind, question, answer = "custom", text, None
        title = "PSST..."
    else:
        kind, question, answer = pick_of_the_day(kind, day, index)
        title = f"{kind.upper()} OF THE DAY  ·  {day:%b %d}"
    first_text, second_text = bubble_texts(kind, question, answer)

    # Canvas size from the preset, scaled to `width` (even sizes for video encoders)
    base_w, base_h, safe_top, safe_bottom, safe_right = SIZES[size]
    width -= width % 2
    height = int(width * base_h / base_w)
    height -= height % 2
    box_top = int(height * safe_top)
    floor_y = height - int(height * safe_bottom)

    # The product fits between the tallest bubble and the bottom safe zone
    blank = Image.new("RGB", (width, height))
    bubble_bottom = max(bubble_layout(blank, t, box_top, safe_right)[-1] for t in (first_text, second_text))
    room = floor_y - bubble_bottom - int(height * 0.06)
    usable_w = width * (1 - safe_right)
    center_x = int(usable_w / 2)
    scale = min(room / product.height, (usable_w * 0.72) / product.width)
    product = product.resize((int(product.width * scale), int(product.height * scale)), Image.LANCZOS)

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
        x = center_x - rotated.width // 2 + offset_x
        y = floor_y - rotated.height
        canvas.paste(rotated, (x, y), rotated)

        body = second_text if t >= 0.5 else first_text
        draw_bubble(canvas, title, body, box_top=box_top, safe_right=safe_right, tail_x=center_x + offset_x,
                    tail_y=y + int(rotated.height * 0.05), accent=accent)
        frame_list.append(canvas)
    return frame_list, question, answer


def save_gif(frame_list, output_path, frame_ms=70):
    # GIFs get every 2nd frame and one shared palette to keep the file small
    frame_list = frame_list[::2]
    palette = frame_list[0].quantize(colors=128, method=Image.MEDIANCUT)
    frame_list = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frame_list]
    frame_list[0].save(output_path, save_all=True, append_images=frame_list[1:],
                       duration=frame_ms, loop=0, optimize=True)


def save_mp4(frame_list, output_path, fps=30, loops=3):
    """H.264 / yuv420p MP4, the format Instagram, TikTok, etc. accept."""
    import imageio.v2 as imageio  # only needed for video

    with imageio.get_writer(output_path, fps=fps, codec="libx264", quality=8,
                            pixelformat="yuv420p", macro_block_size=2,
                            ffmpeg_params=["-movflags", "+faststart"]) as writer:
        for _ in range(loops):
            for frame in frame_list:
                writer.append_data(np.asarray(frame))


def make_animation(product_path, output_path, kind="auto", text=None, day=None, size="reels", width=1080,
                   loops=3, index=0):
    """Save an .mp4 (default) or .gif depending on the output file's extension."""
    is_gif = str(output_path).lower().endswith(".gif")
    frame_list, question, answer = make_frames(product_path, kind=kind, text=text, day=day, size=size,
                                               width=min(width, 600) if is_gif else width, index=index)
    if is_gif:
        save_gif(frame_list, output_path)
    else:
        save_mp4(frame_list, output_path, loops=loops)
    return question, answer


def main():
    parser = argparse.ArgumentParser(description="Turn a product photo into a swaying video/GIF with a joke bubble.")
    parser.add_argument("image", help="path to the product photo")
    parser.add_argument("-o", "--output", help="output path, .mp4 or .gif (default: <image>_<date>.mp4)")
    parser.add_argument("--gif", action="store_true", help="make a GIF instead of an MP4")
    parser.add_argument("--kind", choices=["auto", "joke", "riddle"], default="auto",
                        help="auto alternates jokes and riddles by day")
    parser.add_argument("--text", help="use your own bubble text instead of the joke of the day")
    parser.add_argument("--date", type=date.fromisoformat, help="pick the joke for this date (YYYY-MM-DD)")
    parser.add_argument("--size", choices=SIZES, default="reels",
                        help="reels = 9:16 for TikTok + Instagram Reels/Stories (default), "
                             "feed = 4:5 Instagram post, square = 1:1")
    parser.add_argument("--width", type=int, default=1080, help="width in pixels (GIFs max out at 600)")
    parser.add_argument("--loops", type=int, default=3, help="how many times the MP4 repeats the ~3s loop")
    args = parser.parse_args()

    day = args.date or date.today()
    ext = ".gif" if args.gif else ".mp4"
    output = args.output or str(Path(args.image).with_name(f"{Path(args.image).stem}_{day}{ext}"))
    question, answer = make_animation(args.image, output, kind=args.kind, text=args.text,
                                      day=day, size=args.size, width=args.width, loops=args.loops)
    print(f"Bubble: {question}" + (f"  ->  {answer}" if answer else ""))
    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
