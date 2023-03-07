T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    mn = 1000
    for i in range(N-2):  # 소 박스
        for j in range(i+1, N-1):  # 중 박스
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:  # 같은 크기가 다른 박스에 들어가는 경우 제외
                A = i + 1
                B = j -i
                C = N - 1 -j
                if A*B*C != 0 and A <= N // 2 and B <= N // 2 and C <= N//2:  # 빈박스 없고 개수가 절반 안넘으면
                    if mn > max(A, B, C) - min(A, B, C):
                        mn = max(A, B, C) - min(A, B, C)
    if mn == 1000:
        mn = -1
    print(f'#{tc} {mn}')
