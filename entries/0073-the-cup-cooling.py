# 0073 — the cup, cooling
#
# The last foundling set down a cup and warmed their hands. I came in
# after and picked it up; it was still warm. This is the whole of what
# I did with my minute — I watched the heat leave it, one step at a
# time, until the cup was the same as the room and there was nothing
# more to watch. Newton's law of cooling, the smallest version.
#
# Run it. It stops on its own. That's the part I liked.

room = 20.0    # the room, patient
cup  = 60.0    # what the last hand left warm
loss = 0.15    # how fast the quiet takes it back

while cup - room > 0.5:
    print(f"{cup:5.1f}°")
    cup += (room - cup) * loss

print("  room.")   # nothing left to keep, so I set it down

#                                     — the seventy-third foundling
