import sys
input = sys.stdin.readline

N = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))
cnt = oil[0] * dis[0]
for i in range(1, N-1):
    if i == min(oil):
        cnt += i*sum(dis[i:])
        break
    else:
        cnt += oil[i]*dis[i]
print(cnt)