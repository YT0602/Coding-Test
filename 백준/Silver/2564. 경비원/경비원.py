import sys
input = sys.stdin.readline

x, y = map(int, input().split())
N = int(input())
store = []
cnt = 0
for i in range(N):
    store.append(list(map(int, input().split())))
DG_D, DG_W = map(int, input().split())
for st in store:
    if st[0] == DG_D:
        cnt += abs(DG_W - st[1])
    elif st[0] == 1:
        if DG_D == 1 or DG_D == 2:
            if DG_W + st[1] <= x:
                cnt += (DG_W+y+st[1])
            elif DG_W + st[1] > x:
                cnt += ((2*x - (DG_W+st[1])) + y)
        elif DG_D == 3:
            cnt += DG_W + st[1]
        else:
            cnt += DG_W + (x - st[1])

    elif st[0] == 2:
        if DG_D == 1 or DG_D == 2:
            if DG_W + st[1] <= x:
                cnt += (DG_W+y+st[1])
            elif DG_W + st[1] > x:
                cnt += ((2*x - (DG_W+st[1])) + y)
        elif DG_D == 3:
            cnt += ((y-DG_W) + st[1])
        else:
            cnt += (y-DG_W)+(x-st[1])

    elif st[0] == 3:
        if DG_D == 3 or DG_D == 4:
            if DG_W + st[1] <= y:
                cnt += (DG_W+x+st[1])
            elif DG_W + st[1] > y:
                cnt += ((2*y - (DG_W+st[1])) + x)
        elif DG_D == 1:
            cnt += (DG_W+st[1])
        else:
            cnt += (y-st[1])+DG_W

    elif st[0] == 4:
        if DG_D == 3 or DG_D == 4:
            if DG_W + st[1] <= y:
                cnt += (DG_W+x+st[1])
            elif DG_W + st[1] > y:
                cnt += ((2*y - (DG_W+st[1])) + x)
        elif DG_D == 1:
            cnt += (x-DG_W)+st[1]
        else:
            cnt += (y-st[1])+(x-DG_W)

print(cnt)
