for tc in range(1, 11):
    arr = []
    N = int(input())
    result = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
    dx = [1, -1, 0, 0] # 행 이동
    dy = [0, 0, 1, -1] # 열 이동

    for j in range(N):  # 행
        for k in range(N):  # 열
            for l in range(4):
                if 0 <= j + dx[l] < N and 0 <= k + dy[l] < N:  # 이동한 좌표가 배열 안에 있으면 계산
                    result += abs(arr[j][k] - arr[j + dx[l]][k + dy[l]])
    print(f'#{tc} {result}')
