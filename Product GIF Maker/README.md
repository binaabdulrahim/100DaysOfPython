# Product GIF Maker

Turns a product photo into a **postable MP4 video** (or a GIF): the product sways
side to side while a speech bubble shows the **joke of the day** or **riddle of the day**.

![example](products/bisou_balm_2026-10-05.gif)

Example video: [`products/bisou_balm_2026-10-05.mp4`](products/bisou_balm_2026-10-05.mp4)

**Video format:** H.264 MP4, 30 fps, about 10 seconds (the 3.2 s loop plays 3 times).

| `--size` | Dimensions | Use it for |
|---|---|---|
| `reels` (default) | 1080×1920 (9:16) | **TikTok**, Instagram Reels and Stories |
| `feed` | 1080×1350 (4:5) | Instagram feed post |
| `square` | 1080×1080 (1:1) | Square posts |

The 9:16 layout keeps the bubble and product inside the safe area. That means clear of the top bar, the caption at the bottom and the like/comment/share buttons on the right.

## How it works
1. **Cut out the product.** The script reads the background colour from the top-left corner and flood-fills from the image corners to remove it. Only background touching the edges is removed, so colours inside the product stay.
2. **Pick today's joke.** `jokes.py` holds the jokes and riddles. The date seeds `random`, so the same day always gives the same pick. `--kind auto` gives jokes on even days and riddles on odd days.
3. **Animate.** For each of 96 frames the product is shifted and tilted along a sine wave. The bubble's tail follows the product. A joke's punchline (or a riddle's answer) appears halfway through the loop.

## Usage
```bash
pip install -r requirements.txt
python product_gif.py products/bisou_balm.png                  # 9:16 MP4 for TikTok / Reels
python product_gif.py products/bisou_balm.png --size feed      # 4:5 Instagram post
python product_gif.py products/bisou_balm.png --gif            # GIF instead
python product_gif.py products/bisou_balm.png --kind riddle
python product_gif.py products/bisou_balm.png --text "Kiss dry lips goodbye!"
python product_gif.py products/bisou_balm.png --date 2026-12-25 -o xmas.mp4
```
Works best with a product on a plain, solid-colour background.

## Batch: a video for every product picture
Put the pictures in one folder. They can be named like the scheduled posts, e.g.
`2026-10-05_0700_violette-fr-bisou-balm-in-chocolat.jpg`. Then run:
```bash
python batch_gifs.py sketches/ videos/                 # 9:16 MP4s for TikTok / Reels
python batch_gifs.py sketches/ videos/ --size all      # 9:16 + 4:5 + 1:1
python batch_gifs.py sketches/ videos/ --jobs 4        # render 4 at a time
```
- Videos are made in date/time order and keep the picture's file name.
- Posts alternate between a joke and a riddle. No two posts share one until the lists in `jokes.py` run out (44 of each, so 88 posts).
- `--log beauty_alert_log.txt` takes the product list from a log file instead, and matches each product to a picture by name.
