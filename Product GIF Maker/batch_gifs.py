"""Make a postable MP4 (or GIF) for every product in the Beauty Alert Log.

Each log line looks like:   2026-10-05 | topic | Violette_FR Bisou Balm in Chocolat
The script finds the matching picture in the images folder (by name), and uses
the log date to pick that day's joke / riddle.

Usage:
    python batch_gifs.py beauty_alert_log.txt products/ videos/
"""

import argparse
import difflib
import re
import unicodedata
from datetime import date
from pathlib import Path

from product_gif import SIZES, make_animation

IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}


def slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def read_log(log_path):
    entries = []
    for line in Path(log_path).read_text(encoding="utf-8").splitlines():
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 3 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", parts[0]):
            entries.append((date.fromisoformat(parts[0]), parts[2].replace("\\_", "_")))
    return entries


def find_image(product, images):
    """Match on file name: exact, then contained, then closest spelling."""
    target = slug(product)
    by_slug = {slug(p.stem): p for p in images}
    if target in by_slug:
        return by_slug[target]
    for name, path in by_slug.items():
        if name in target or target in name:
            return path
    # Fuzzy match only among files from the same brand (first word), so similar
    # product names from different brands don't get mixed up
    brand = target.split("_")[0]
    same_brand = [name for name in by_slug if name.split("_")[0] == brand]
    close = difflib.get_close_matches(target, same_brand, n=1, cutoff=0.6)
    return by_slug[close[0]] if close else None


def main():
    parser = argparse.ArgumentParser(description="Make a joke-bubble GIF for every product in the log.")
    parser.add_argument("log", help="text file with 'date | topic | product' lines")
    parser.add_argument("images", help="folder with one picture per product")
    parser.add_argument("output", help="folder to save GIFs into")
    parser.add_argument("--kind", choices=["auto", "joke", "riddle"], default="auto")
    parser.add_argument("--gif", action="store_true", help="make GIFs instead of MP4s")
    parser.add_argument("--size", choices=list(SIZES) + ["all"], default="reels",
                        help="reels = 9:16 TikTok/Reels (default), feed = 4:5 Instagram post, square, or all")
    args = parser.parse_args()

    images = [p for p in Path(args.images).iterdir() if p.suffix.lower() in IMAGE_TYPES]
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    made, missing = 0, []
    entries = read_log(args.log)
    for n, (day, product) in enumerate(entries):
        index = sum(1 for d, _ in entries[:n] if d == day)  # nth product that day -> its own joke
        image = find_image(product, images)
        if not image:
            missing.append(f"{day}  {product}")
            continue
        for size in (SIZES if args.size == "all" else [args.size]):
            output = out_dir / f"{day}_{slug(product)}_{size}{'.gif' if args.gif else '.mp4'}"
            make_animation(image, output, kind=args.kind, day=day, size=size, index=index)
            made += 1
        print(f"✓ {day}  {product}  ({image.name})")

    print(f"\nMade {made} file(s) in {out_dir}/")
    if missing:
        print(f"No picture found for {len(missing)} product(s):")
        print("\n".join(f"  - {m}" for m in missing))


if __name__ == "__main__":
    main()
