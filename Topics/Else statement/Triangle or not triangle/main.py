triangle_sum = 180

first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

if triangle_sum == first_angle + second_angle + third_angle:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
