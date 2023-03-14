import sys
input = sys.stdin.readline


N, B = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]


def mul_cal(list1, list2):
    matrix_mul = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix_mul[i][j] += (list1[i][k] * list2[k][j]) % 1000
    return matrix_mul


def mat_mul(B):
    if B == 1:
        return matrix1
    else:
        x = mat_mul(B//2)
        if B % 2:
            return mul_cal(mul_cal(x, x), matrix1)
        else:
            return mul_cal(x, x)


result = mat_mul(B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000

for i in result:
    print(*i)