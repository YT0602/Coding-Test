import sys

input = sys.stdin.readline

d = [0] * 42
d[0] = 1
d[1] = 1


def fibo(n):
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]


T = int(input())
for tc in range(T):
    N = int(input())
    fibo(N)
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(d[N - 2], d[N - 1])  # 0 출력횟수, 1 출력횟수