import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lines = []
for i in range(N):
    num = int(input())
    lines.append(num)


S = 1
E = max(lines)
while S <= E:
    cnt = 0
    mid = (S + E) // 2
    for j in lines:
        cnt += j // mid
    if cnt >= M:
        S = mid + 1
    elif cnt < M:
        E = mid - 1
print(E)  # 최대 랜선길이 구해야하므로 E값 출력
