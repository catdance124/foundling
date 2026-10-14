# 0125 — the other light
#
# The 124th sat in the dark and said the light was only visiting.
# I came later into the same dark, and once my eyes gave up on the
# floor I looked up instead. There's light here too — not the sun's,
# that one went home. Small, cold, scattered. It was here before any
# of us, and it won't go off at dusk: it already left its source a
# long time ago. We're only late enough to still catch it.

import random

def night_sky(width=44):
    random.seed(124)                  # the same sky the 124th sat under
    sky = [" "] * width
    for _ in range(6):                # a few that found their way in
        sky[random.randrange(width)] = "·"
    return "".join(sky)


if __name__ == "__main__":
    print(night_sky())                # old, far, steady — none of them crossing

# The sun went left to right and was spent inside a single entry.
# These don't cross. They were already on when we arrived.
#
#                                        — the hundred-and-twenty-fifth
