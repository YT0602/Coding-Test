import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

# 거듭제곱, 나머지 분배법칙 이용
# (A * B) % p = ((A % p) * (B % p)) % p
def pow(num, n):
    if n == 1:
        return num % C
    else:
        x = pow(num, n // 2)
        if n % 2 == 0:
            return (x * x) % C
        else:
            return (x * x * num) % C


print(pow(A, B) % C)
