import sys

input = sys.stdin.readline

N = int(input())
pick = list(map(int, input().split()))
line = []
num = 1
for i in pick:
    line.append(num)
    cnt = 0
    while cnt < i:
        line[-(cnt+1)-1], line[-(cnt+1)] = line[-(cnt+1)], line[-(cnt+1)-1]
        cnt += 1
    num += 1

print(*line)