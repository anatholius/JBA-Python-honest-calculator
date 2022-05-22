box = sorted([int(input()) for _ in range(3)])
door = sorted([int(input()) for _ in range(2)])

print("The box cannot be carried"
      if box[1] > door[1] or box[0] > door[0]
      else "The box can be carried")
