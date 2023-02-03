import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    numbers = list(map(int, input().split()))
    arr.append(numbers)

M = 0
x = 1
y = 1
for i in range(len(arr)):
    if M < max(arr[i]):
        M = max(arr[i])
        x = i+1
        y = arr[i].index(M) + 1


print(M)
print(x, y)