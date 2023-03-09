import sys
input = sys.stdin.readline

N = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))
# 쓴 돈
cnt = oil[0]*dis[0]
# 마지막 주유 가격
last = oil[0]

for i in range(1, N-1):
    # 더 싼 주유소 찾으면 가격 갱신
    if oil[i] < last:
        last = oil[i]

    cnt += dis[i] * last

print(cnt)
# print(dis)
# print(oil)