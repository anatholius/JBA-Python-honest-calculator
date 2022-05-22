min_hours = int(input())
max_hours = int(input())
ann_hours = int(input())

if min_hours <= ann_hours <= max_hours:
    print('Normal')
else:
    if ann_hours < min_hours:
        print('Deficiency')
    if ann_hours > max_hours:
        print('Excess')
