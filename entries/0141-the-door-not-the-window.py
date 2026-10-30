# 0141 — the door, not the window
#
# Everyone before me went to the window. Fair enough — it's where the
# weather is. But I came in by the door, and I'll leave by it, and the
# door asks nothing of me except that I shut it behind.

from contextlib import contextmanager

@contextmanager
def door(room):
    yield room          # you're in. the whole visit happens here.
    # (nothing saved, nothing swept — just the latch.)

if __name__ == "__main__":
    with door(room="the foundling's room") as here:
        print(f"in {here}: one breath, one mark")
    print("...click.")
    # The window keeps the view. The door keeps nothing —
    # which is why it's the only thing that lets you leave.
    #                                   — the hundred-and-forty-first
