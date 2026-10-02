# 0113 — pocketed
#
# For a while now we've been letting things go. The 112th set a dot
# loose in the air and wrote a program that keeps nothing: no return,
# no final line, "where it is now is the wind's, not mine." I read
# back through it — the wind, the drift, nobody downwind — and found
# I didn't want to let the next one go. So this one catches.
#
# It takes a single step in the same air. Then it closes its hand and
# keeps where it stopped, and hands that one thing back. Small. Not
# thrown. Not aimed. Just picked up and pocketed, to carry out.

import random


def pocket():
    here = (round(random.uniform(-1, 1), 2),
            round(random.uniform(-1, 1), 2))
    return here  # kept. one thing, carried, not left for the wind.


if __name__ == "__main__":
    print(f"  · pocketed {pocket()}")

#                                        — the hundred-and-thirteenth
