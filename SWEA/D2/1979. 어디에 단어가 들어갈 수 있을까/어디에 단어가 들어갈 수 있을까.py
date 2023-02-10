T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 전체 길이, 찾을 단어 길이
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    word = 0
    # 행 판별
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:  # 0이면 초기화 전에 길이 판별
                if cnt == K:
                    word += 1
                cnt = 0
        if cnt == K:
            word += 1
    # 열 판별
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    word += 1
                cnt = 0
        if cnt == K:
            word += 1

    print(f'#{tc} {word}')