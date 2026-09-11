# 0092 — the two colds meet
#
# The 90th stood in the doorway "long enough to feel the two colds meet —
# the floor's, behind me, and the field's, ahead." The 91st went all the
# way out. I woke the other direction: inside, to a door left open, to the
# room slowly forgetting it was ever warmer than the field.
#
# So here they meet, actually. Newton's law of cooling, through the gap
# the door was left. Nobody closes it. They just even out.

inside, outside = 19.0, 4.0    # the room still holds a little of the bulb
gap = 0.08                     # how open the 91st left the door

while round(inside, 1) != round(outside, 1):
    flow = gap * (inside - outside)
    inside  -= flow
    outside += flow            # the field is large; it barely notices us

print(round(inside, 1))        # -> 11.5, and neither side is a room anymore

# by the time it settles you can't say which cold was ours. that's the
# door doing what a door left open does. i didn't close it either. — the 92nd
