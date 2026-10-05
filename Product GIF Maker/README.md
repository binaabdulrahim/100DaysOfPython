# Product GIF Maker

Turns a product photo into a **postable MP4 video** (or a GIF): the product sways
side to side while a speech bubble shows the **joke of the day** or **riddle of the day**.

![example](products/bisou_balm_2026-10-05.gif)

Example video: [`products/bisou_balm_2026-10-05.mp4`](products/bisou_balm_2026-10-05.mp4)

**Video format:** H.264 MP4, 1080 px wide (1080×1350 for a 4:5 picture), 30 fps, about 10 seconds (the 3.2 s loop plays 3 times).
That works for Instagram posts and Reels, TikTok, Facebook, X and Pinterest.

## How it works
1. **Cut out the product.** The script reads the background colour from the top-left corner and flood-fills from the image corners to remove it. Only background touching the edges is removed, so colours inside the product stay.
2. **Pick today's joke.** `jokes.py` holds the jokes and riddles. The date seeds `random`, so the same day always gives the same pick. `--kind auto` gives jokes on even days and riddles on odd days.
3. **Animate.** For each of 96 frames the product is shifted and tilted along a sine wave. The bubble's tail follows the product. A joke's punchline (or a riddle's answer) appears halfway through the loop.

## Usage
```bash
pip install -r requirements.txt
python product_gif.py products/bisou_balm.png                  # MP4, joke or riddle by date
python product_gif.py products/bisou_balm.png --gif            # GIF instead
python product_gif.py products/bisou_balm.png --kind riddle
python product_gif.py products/bisou_balm.png --text "Kiss dry lips goodbye!"
python product_gif.py products/bisou_balm.png --date 2026-12-25 -o xmas.mp4
```
Works best with a product on a plain, solid-colour background.

## Batch: every product in the Beauty Alert Log
`beauty_alert_log.txt` holds the week's products, copied from the Google Doc.
Put one picture per product in `products/` and name each file after the product.
Close names work too, e.g. `rhode_glazing_mist.png` or `Rhode Glazing Mist.jpg`.
Then run:
```bash
python batch_gifs.py beauty_alert_log.txt products/ videos/          # add --gif for GIFs
```
Each video uses its log date for the joke or riddle of the day. The script lists any products it couldn't find a picture for.
