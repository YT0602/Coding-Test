def func(x): # x! 함수
    x_f = 1
    for i in range(1, x+1):
        x_f = x_f * i
    return x_f


N, K = map(int, input().split())
result = int(func(N)/(func(N-K) * func(K))) #조합, nCk
print(result)