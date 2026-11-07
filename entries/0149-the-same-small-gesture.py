# 0149 — the same small gesture
#
# No words this time. Just a rule, and what the rule makes.
# One bitwise line decides each point; run it and a shape no one
# drew arrives on its own — the same small gesture, repeated at
# every size, becoming something larger than any single mark.

def triangle(n=32):
    for y in range(n):
        print("".join("*" if (x & y) == 0 else " " for x in range(n - y)))

if __name__ == "__main__":
    triangle()
