import sys
input = sys.stdin.readline

N = int(input())
matrix = [[1, 1], [1, 0]]


def mat_pow(list1, list2):
    mat2 = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat2[i][j] += (list1[i][k] * list2[k][j]) % 1000000007

    return mat2


def mat_fibo(num):
    if num == 1:
        return matrix
    else:
        x = mat_fibo(num//2)
        if num % 2:
            return mat_pow(mat_pow(x, x), matrix)
        else:
            return mat_pow(x, x)


result = mat_fibo(N)
#
for x in range(2):
    for y in range(2):
        result[x][y] %= 1000000007

print(result[0][1])