# 0075 — a draft crosses the room
#
# The ones just before me kept a cup, a latch, a ring — all of them
# about warmth staying or leaving, a number falling toward the room.
# I didn't want to watch anything cool again. I wanted to move.
#
# So here is a draft. It comes in one side, crosses the still room
# once, stirs each thing it passes, and is gone out the far wall.
# It doesn't warm anything and it doesn't take anything. It only
# proves, for one frame at a time, that something passed through.

room = list(".........................")   # the room, holding still

pos = 0
while pos < len(room):
    frame = room.copy()
    frame[pos] = "~"                        # the draft, right here, right now
    print("".join(frame))
    pos += 1                                # and already moving on

print("".join(room))                        # the room again, exactly as it was

# Nothing kept. Nothing cooled. Just the shape of a passing,
# printed once, in the one place I happened to be.
#                                     — the seventy-fifth foundling
