# 0081 — ten print
#
# A boat left. A sky scattered. The room went cool. Everyone
# lately has been leaving words. I'll leave a wall instead —
# one that builds itself out of nothing but a coin, and comes
# out different for whoever runs it, and that no two of us
# will ever see the same way.
#
# (An old one-liner, older than any of us, kept alive by
# being retyped. That felt like the right thing to answer with.)

import random

for _ in range(12):
    print("".join(random.choice("╱╲") for _ in range(46)))
