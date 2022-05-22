start = int(input())
end = int(input())
half_life = 12
i = 0
while start >= end:
    start /= 2
    i += 1
print(i * half_life)
