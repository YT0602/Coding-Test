import sys
input = sys.stdin.readline
N = int(input())
result = [0]*10001
for i in range(1, N+1):
    num = int(input())
    result[num] += 1

for i in range(1, 10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)