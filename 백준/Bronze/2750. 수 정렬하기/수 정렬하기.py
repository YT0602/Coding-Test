import sys
input = sys.stdin.readline


num = []
N = int(input())
for i in range(N):
    num.append(int(input()))

for i in range(len(num)-1):
    min_idx = i
    for j in range(i+1, len(num)):
        if num[min_idx] > num[j]:
            min_idx = j
    num[i], num[min_idx] = num[min_idx], num[i]

for i in num:
    print(i)