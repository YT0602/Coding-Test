import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
s = 0
e = N - 1
ans = 2000000000
num1 = 0
num2 = 0

while s < e:
    if abs(numbers[s] + numbers[e]) == 0:
        ans = 0
        num1 = numbers[s]
        num2 = numbers[e]
        break
    elif abs(numbers[s] + numbers[e]) < abs(ans):
        num1 = numbers[s]
        num2 = numbers[e]
        ans = numbers[s] + numbers[e]
    if numbers[s] + numbers[e] > 0:
        e -= 1
    else:
        s += 1

# print(ans)
print(num1, num2)
