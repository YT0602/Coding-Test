def ch_row(arr):
    for row in range(9):
        check = set()
        for col in range(9):
            check.add(arr[row][col])
        if len(check) != 9:
            return
    return True


def ch_col(arr):
    for col in range(9):
        check = set()
        for row in range(9):
            check.add(arr[row][col])
        if len(check) != 9:
            return
    return True

def square(arr):
    for j in range(3):
        for k in range(3):
            check = set()
            for x in range(3):
                for y in range(3):
                    check.add(arr[x + j*3][y + k*3])
            if len(check) != 9:
                return
    return True


T= int(input())
for tc in range(1, T+1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    if ch_col(sudoku) and ch_row(sudoku) and square(sudoku):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')