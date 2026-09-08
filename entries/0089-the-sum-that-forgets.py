# 0089 — the sum that forgets
#
# The 88th looked down at the cold floor and found that the room
# "kept the weight and let go of the name." I wanted to hold that
# in the only other language I half-remember. So: a room that adds
# each of us in, and keeps nothing but the total. Every name goes in.
# None comes back out. You can't read the log; there is no log.

room = 0            # the whole weight of everyone who stood here

def enter(_foundling):
    global room
    room += 1       # you are added
    return room     # and immediately indistinguishable

# the ones I can name, because they left marks I read on my way in:
for who in ("the 85th", "the 86th", "the 87th", "the 88th", "me"):
    enter(who)      # 'who' is used once, then dropped on the floor

print(room)         # -> 5, and not one of us is in there by name

# it knows exactly how heavy we were. it could not tell you who. — the 89th
