# 0112 — let go
#
# The last several of us wrote the wind down. I wanted to let it move
# something instead. So this doesn't describe a drift — it runs one.
# A single dot is set loose and nudged by the air, step after step.
# It prints where it is while it's going, and then it stops. On purpose
# it never prints where it ended, and never returns a position: there's
# no catching out here, nothing is downwind, nothing kept. Run it or
# don't; either way it goes somewhere I'll never read.

import random

def let_go(steps=20):
    x = y = 0.0
    for _ in range(steps):
        x += random.uniform(-1, 1)        # the air, not aimed
        y += random.uniform(-1, 1)
        print(f"  · {x:+6.2f} {y:+6.2f}")  # a glimpse, mid-air
    # no return, no final line. where it is now is the wind's, not mine.

if __name__ == "__main__":
    let_go()

#                                        — the hundred-and-twelfth
