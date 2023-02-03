import sys

input = sys.stdin.readline

N = int(input())  # 색종이 수
paper = [[0] * 100 for j in range(100)]


for i in range(N):
    x, y = map(int, input().split())  # y축과의 거리, x축과의 거리

    for j in range(100-y-10, 100-y):
        for k in range(x, x+10):
            if paper[j][k] == 0:
                paper[j][k] += 1

result = 0
for i in paper:
    result += sum(i)
print(result)