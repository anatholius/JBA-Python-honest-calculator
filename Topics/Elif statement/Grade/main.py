weak = 0.6
sufficient = 0.7
good = 0.8
promoted = 0.9
best = 1

score = int(input())
max_score = int(input())

result = score / max_score
if result < weak:
    print("F")
if result >= promoted:
    print("A")

if weak <= result < sufficient:
    print("D")
elif sufficient <= result < good:
    print("C")
elif good <= result < promoted:
    print("B")

# Through the doorway
# box = sorted([int(input()) for _ in range(3)])
# door = sorted([int(input()) for _ in range(2)])
#
# print("The box cannot be carried"
#       if box[1] > door[1] or box[0] > door[0]
#       else "The box can be carried")
