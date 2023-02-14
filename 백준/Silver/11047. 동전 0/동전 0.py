import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
cnt = 0
for i in range(N):
    coin.append(int(input()))
coin.reverse()
for i in coin:
    if i <= K:
        cnt += K//i
        K %= i
        if K == 0:
            break

print(cnt)