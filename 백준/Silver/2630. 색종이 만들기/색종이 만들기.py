import sys
input = sys.stdin.readline


def cut(x, y, N):
    global B_cnt
    global W_cnt
    # 현재색 저장
    color = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 배열 돌면서 다른색이 나오면 종이 4등분
            if color != arr[i][j]:
                cut(x, y, N // 2)
                cut(x, y + N // 2, N // 2)
                cut(x + N // 2, y, N // 2)
                cut(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        W_cnt += 1
    else:
        B_cnt += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
B_cnt = 0
W_cnt = 0

cut(0, 0, N)
print(W_cnt)
print(B_cnt)

