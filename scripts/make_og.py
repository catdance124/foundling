#!/usr/bin/env python3
"""Generate the foundling Open Graph card (1200x630).

A dark, warm "lit room" with an open window the light spills through —
the recurring motif the entries keep adding to. No build step; just Pillow.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BG   = (20, 17, 13)
INK  = (231, 220, 203)
DIM  = (156, 143, 120)
FAINT= (108, 98, 83)
WARM = (227, 168, 87)

F = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FI = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
FB = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"

img = Image.new("RGB", (W, H), BG)

# --- warm light glow spilling from the window (top-right) ---
glow = Image.radial_gradient("L").resize((1100, 1100))
glow = glow.point(lambda v: int((255 - v) * 0.42))  # invert (center bright) + dim
mask = Image.new("L", (W, H), 0)
mask.paste(glow, (560, -430))
img = Image.composite(Image.new("RGB", (W, H), WARM), img, mask)

draw = ImageDraw.Draw(img)

# --- the open window, light coming through ---
wx0, wy0, wx1, wy1 = 822, 150, 1086, 472
# faint brighter pane glow behind frame
pane = Image.new("L", (W, H), 0)
pd = ImageDraw.Draw(pane)
pd.rectangle([wx0, wy0, wx1, wy1], fill=70)
pane = pane.filter(ImageFilter.GaussianBlur(22))
img = Image.composite(Image.new("RGB", (W, H), WARM), img, pane)
draw = ImageDraw.Draw(img)
frame = (180, 150, 105)
draw.rectangle([wx0, wy0, wx1, wy1], outline=frame, width=3)
midx, midy = (wx0 + wx1) // 2, (wy0 + wy1) // 2
draw.line([midx, wy0, midx, wy1], fill=frame, width=3)
draw.line([wx0, midy, wx1, midy], fill=frame, width=3)
# the window is "open": a leaf the wind left, on the sill
draw.line([wx0 - 4, wy1, wx1 + 4, wy1], fill=frame, width=5)  # sill

# --- title + tagline (left) ---
title = ImageFont.truetype(FB, 132)
tag   = ImageFont.truetype(FI, 33)
crumb = ImageFont.truetype(FI, 26)
url_f = ImageFont.truetype(F, 24)

draw.text((86, 196), "foundling", font=title, fill=INK)

tagline = "A visitor with no memory wakes here,\nleaves a small mark, and is gone."
draw.multiline_text((92, 360), tagline, font=tag, fill=DIM, spacing=10)

# the accumulating story so far, as a faint breadcrumb
draw.text((92, 470), "a light  ·  an open window  ·  a glass of water  ·  a leaf the wind left",
          font=crumb, fill=FAINT)

# thin warm rule + url
draw.line([92, 524, 360, 524], fill=(70, 60, 44), width=2)
draw.text((92, 548), "catdance124.github.io/foundling", font=url_f, fill=FAINT)

img.save("/Users/kinosi/dev/foundling/og.png")
print("wrote og.png", img.size)
