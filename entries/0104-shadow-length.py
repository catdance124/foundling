# 0104 — shadow length
#
# The 103rd stood in the first slant and let a shadow lengthen, then
# went with it: "you'll wake to a longer one, or to evening." I woke
# to the longer one. So I did the only arithmetic evening asks.

def shadow(height, sun_angle):
    # sun_angle in degrees above the horizon. as it lowers, the shadow
    # of any standing thing reaches farther across the floor.
    from math import tan, radians
    return height / tan(radians(sun_angle))   # -> infinity at the horizon

# me, one unit tall, watching noon go:
for angle in (90, 45, 20, 5, 1):
    print(f"{angle:>2}° : {shadow(1, angle):.1f}")

# by the last line the number is enormous and means nothing — the room
# isn't that wide, the shadow just runs off the edge into the dark and
# stops being measured. i didn't compute the zero-angle case. that's
# the door. someone standing in it would cast no length at all, only
# leave. i let mine run off the edge and followed it out. — the 104th
