def comb(num, idx, list):
    global cnt
    if sum(list) == num:
        cnt += 1
        return
    if sum(list) > num:
        return
    for i in range(idx, N):
        if v[i] == 0:
            v[i] = 1
            comb(num, i+1, list + [numbers[i]])
            v[i] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    v = [0] * N
    cnt = 0
    result = []

    comb(K, 0, result)

    print(f'#{tc} {cnt}')
