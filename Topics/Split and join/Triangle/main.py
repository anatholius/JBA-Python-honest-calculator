h = int(input())
w = (h - 1) * 2 + 1
print('\n'.join([('#' * (i * 2 + 1)).center(w) for i in range(h)]))
