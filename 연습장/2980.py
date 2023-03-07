N, L = map(int, input().split())
t = 0
now = 0

for i in range(N):
    D, R, G = map(int, input().split())
    # 다음 신호등까지 시간
    next = t + D - now
    # 나머지가 R 보다 작으면 대기해야됨
    if next % (R+G) == 0:
        t += R+D-now
        now = D
    elif next % (R+G) < R:
        t += (R - (next % (R+G))) + D-now
        now = D
    elif next % (R+G) >= R:
        t += D-now
        now = D

t += L-now
print(t)



