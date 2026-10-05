"""Make a postable MP4 (or GIF) for every product picture in a folder.

Pictures named like the scheduled posts, e.g.
    2026-10-05_0700_violette-fr-bisou-balm-in-chocolat.jpg
are put in date/time order. Posts alternate joke / riddle, and no two posts share
a joke or riddle until the lists in jokes.py run out.

Usage:
    python batch_gifs.py sketches/ videos/
    python batch_gifs.py sketches/ videos/ --size all --jobs 4

Older mode: pass --log beauty_alert_log.txt to take the product list from the log
and match each product to a picture by name.
"""

import argparse
import difflib
import re
import unicodedata
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path

from product_gif import SIZES, make_animation, pick_for_post

IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".webp"}
SCHEDULED_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})_(\d{4})_(.+)")


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
    by_slug = {slug(SCHEDULED_NAME.sub(r"\3", p.stem)): p for p in images}
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


def posts_from_folder(images):
    """(date, label, image) for every picture, in date/time order."""
    posts = []
    for image in sorted(images, key=lambda p: p.name):
        match = SCHEDULED_NAME.fullmatch(image.stem)
        day = date.fromisoformat(match[1]) if match else date.today()
        posts.append((day, image.stem, image))
    return posts


def render(job):
    image, output, kind, day, size, pick = job
    make_animation(image, output, kind=kind, day=day, size=size, pick=pick)
    return output


def main():
    parser = argparse.ArgumentParser(description="Make a joke-bubble video for every product picture.")
    parser.add_argument("images", help="folder with one picture per product")
    parser.add_argument("output", help="folder to save videos into")
    parser.add_argument("--log", help="optional 'date | topic | product' log to take the product list from")
    parser.add_argument("--kind", choices=["auto", "joke", "riddle"], default="auto",
                        help="auto alternates joke / riddle from post to post")
    parser.add_argument("--gif", action="store_true", help="make GIFs instead of MP4s")
    parser.add_argument("--size", choices=list(SIZES) + ["all"], default="reels",
                        help="reels = 9:16 TikTok/Reels (default), feed = 4:5 Instagram post, square, or all")
    parser.add_argument("--jobs", type=int, default=3, help="videos to render at the same time")
    args = parser.parse_args()

    images = [p for p in Path(args.images).iterdir() if p.suffix.lower() in IMAGE_TYPES]
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    missing = []
    if args.log:
        posts = []
        for day, product in read_log(args.log):
            image = find_image(product, images)
            if image:
                posts.append((day, f"{day}_{slug(product)}", image))
            else:
                missing.append(f"{day}  {product}")
    else:
        posts = posts_from_folder(images)

    sizes = list(SIZES) if args.size == "all" else [args.size]
    ext = ".gif" if args.gif else ".mp4"
    jobs = []
    for n, (day, label, image) in enumerate(posts):
        pick = pick_for_post(n, args.kind)
        for size in sizes:
            name = f"{label}{'_' + size if len(sizes) > 1 else ''}{ext}"
            jobs.append((image, out_dir / name, args.kind, day, size, pick))

    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        for i, output in enumerate(pool.map(render, jobs), 1):
            print(f"✓ [{i}/{len(jobs)}] {output.name}", flush=True)

    print(f"\nMade {len(jobs)} file(s) in {out_dir}/")
    if missing:
        print(f"No picture found for {len(missing)} product(s):")
        print("\n".join(f"  - {m}" for m in missing))


if __name__ == "__main__":
    main()
