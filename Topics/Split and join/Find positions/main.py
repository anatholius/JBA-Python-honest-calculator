seq, x = enumerate(input().split()), input()
print(' '.join([str(pos) for pos, num in seq if num == x]) or 'not found')
