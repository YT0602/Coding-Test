import sys
input = sys.stdin.readline

N = int(input())
# 기본행렬
# [[1, 1], [1, 0]] **n = [[F(n+1), F(n)], [F(n), F(n-1)]]
# 피보나치 행렬 이용
matrix = [[1, 1], [1, 0]]

# 행렬 제곱 합수
def mat_pow(list1, list2):
    mat2 = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                # 나머지 분배법칙
                mat2[i][j] += (list1[i][k] * list2[k][j]) % 1000000
    return mat2


def mat_fibo(num):
    if num == 1:
        return matrix
    else:
        # 거듭제곱 원리 이용
        x = mat_fibo(num//2)
        # 홀수면 행렬 제곱에 기본행렬 곱셈
        if num % 2:
            return mat_pow(mat_pow(x, x), matrix)
        # 짝수면 행렬 제곱
        else:
            return mat_pow(x, x)


result = mat_fibo(N)
# 결과값 나머지로 변환
for x in range(2):
    for y in range(2):
        result[x][y] %= 1000000
# F(n) 출력
print(result[0][1])