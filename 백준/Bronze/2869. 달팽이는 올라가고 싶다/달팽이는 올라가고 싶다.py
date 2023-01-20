import math
A, B, V = map(int, input().split())
day_height = A - B
day = math.ceil((V - A) / day_height) + 1

print(day)