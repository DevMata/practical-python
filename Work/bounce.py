# bounce.py
#
# Exercise 1.5
height = 100
bounce_ratio = 3/5

for i in range(1, 11):
    height = height * bounce_ratio
    print(i, round(height, 4))
