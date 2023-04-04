import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = M-N+1
v = [False] * (M-N+1)
i = 2
# 최대값보다 작은 제곱 수까지만
while i * i <= M:
    x = i*i
    # 범위안에서 제곱수로 나누어 떨이지는 수 중 가장 작은 값 찾기
    # 제곱수랑 곱할 몫 찾기
    if N % x == 0:
        y = N // x
    else:
        y = N // x + 1
    while x * y <= M:
        # 체로 거르기
        if not v[x*y-N]:
            v[x*y-N] = True
            ans -= 1
        # 제곱수의 배수 점점 증가
        y += 1
    # 제곱수 점점 증가
    i += 1
print(ans)