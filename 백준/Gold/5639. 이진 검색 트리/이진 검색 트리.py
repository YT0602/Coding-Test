import sys
sys.setrecursionlimit(10**9)
num = []
while True:
    try:
        N = int(input())
        num.append(N)

    except:
        break


def post(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if num[s] < num[i]:
            mid = i
            break
    post(s+1, mid-1)
    post(mid, e)
    print(num[s])

post(0, len(num)-1)