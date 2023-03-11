import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    st = [list(map(int, input().split())) for _ in range(2)]
    if len(st[0]) >= 2:
        st[1][1] += st[0][0]
        st[0][1] += st[1][0]
        if len(st[0]) > 2:
            for i in range(2, N):
                st[0][i] += max(st[1][i-1], st[1][i-2])
                st[1][i] += max(st[0][i-1], st[0][i-2])
    print(max(st[0][-1], st[1][-1]))