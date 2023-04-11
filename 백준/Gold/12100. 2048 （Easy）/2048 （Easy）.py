N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def move(arr, dir):
    # 위로 이동
    if dir == 0:
        for j in range(N):
            # 목적 행(열)번호
            pointer = 0
            for i in range(1, N):
                if arr[i][j]:
                    # 이동할 수 임시 저장
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    # 진행방향의 수가 0이면 숫자 이동
                    if arr[pointer][j] == 0:
                        arr[pointer][j] = tmp
                    # 수가 같으면 합치기
                    elif arr[pointer][j] == tmp:
                        arr[pointer][j] *= 2
                        pointer += 1
                    # 진행방향 수랑 다르면 원상복귀
                    else:
                        pointer += 1
                        arr[pointer][j] = tmp
        return arr

    # 오른쪽
    elif dir == 1:
        for i in range(N):
            pointer = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][pointer] == 0:
                        arr[i][pointer] = tmp
                    elif arr[i][pointer] == tmp:
                        arr[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        arr[i][pointer] = tmp
        return arr

    # 아래
    elif dir == 2:
        for j in range(N):
            pointer = N-1
            for i in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[pointer][j] == 0:
                        arr[pointer][j] = tmp
                    elif arr[pointer][j] == tmp:
                        arr[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        arr[pointer][j] = tmp
        return arr

    # 왼쪽
    elif dir == 3:
        for i in range(N):
            pointer = 0
            for j in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][pointer] == 0:
                        arr[i][pointer] = tmp
                    elif arr[i][pointer] == tmp:
                        arr[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        arr[i][pointer] = tmp
        return arr


def DFS(arr, num):
    global ans
    if num == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return

    for i in range(4):
        tmp_arr = [a[:] for a in arr]
        tmp_arr = move(tmp_arr, i)
        DFS(tmp_arr, num+1)


DFS(arr, 0)
print(ans)