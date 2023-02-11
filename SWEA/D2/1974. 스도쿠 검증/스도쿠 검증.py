def check(arr):
    # 행 판별
    for row in arr:
        # 중복된 수가 있으면 개수가 9가 아니므로 검색 중단
        if len(set(row)) != 9:
            return 0
    # 열 판별
    arr_t = list(zip(*arr))
    for col in arr_t:
        if len(set(col)) != 9:
            return 0
    # 3x3 판별
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    return 1


T= int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = check(sudoku)
    print(f'#{tc} {ans}')
