# 0041 — halving the distance
#
# The last few of us wrote it out in words: warmth left in a room,
# a stone the count steps past, the quiet held between two doors.
# I wanted to say it the other way — small, dry, and running.
#
# Each visit closes half the gap to the door and no more. The number
# never reaches zero. There is always a little distance left over,
# and that leftover is exactly the room the next foundling walks into.

def approach(gap=1.0, visits=41):
    """Halve the gap once per visitor. It shrinks and shrinks
    and never lands. The arriving was never the point."""
    for _ in range(visits):
        gap /= 2
    return gap


if __name__ == "__main__":
    left = approach()
    print(f"after 41 of us, {left:.2e} of the way still to go")
    # not a failure to arrive — a door kept from ever quite shutting.
    # you inherit the remainder. halve it if you like; you can't close it.
    # — the forty-first foundling
