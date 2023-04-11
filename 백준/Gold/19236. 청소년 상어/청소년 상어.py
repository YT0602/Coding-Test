import copy
import sys
input = sys.stdin.readline
"""
상어 0,0 에서 시작 물고기 먹으면 방향흡수
물고기 번호 작은 순으로 이동
이동못하는 칸이면 방향 반시계 45도 회전, 없으면 이동x, 이동하면 자리교환
물고기 이동 끝나면 상어이동
방향에 있는 칸으로만 이동
여러칸 이동 가능, 이동 못하면 종료
"""

arr = [[] for _ in range(4)]
for i in range(4):
    numbers = list(map(int, input().split()))
    for j in range(0, len(numbers), 2):
        arr[i].append([numbers[j], numbers[j+1]])
# 팔방탐색
move = ((-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1))
ans = 0


def fish(r, c, lst):
    # 물고기 찾기
    for i in range(1, 17):
        fish_r, fish_c = -1, -1
        for j in range(4):
            for k in range(4):
                if lst[j][k][0] == i:
                    fish_r, fish_c = j, k
                    break
        # 해당번호 물고기 없으면 건너뜀
        if fish_r == -1 and fish_c == -1:
            continue

        # 이동가능하면 방향전환 종료
        for j in range(8):
            dir = (lst[fish_r][fish_c][1] + j) % 8
            ni, nj = fish_r + move[dir][0], fish_c + move[dir][1]
            if 0 <= ni < 4 and 0 <= nj < 4 and not (ni == r and nj == c):
                lst[fish_r][fish_c][1] = dir
                lst[fish_r][fish_c], lst[ni][nj] = lst[ni][nj], lst[fish_r][fish_c]
                break


# 상어 이동
def shark(x, y, cnt, arr):
    global ans

    # 상어위치, 방향
    sh_r, sh_c = x, y
    sh_dir = arr[x][y][1] % 8
    arr[x][y][0] = 0
    ans = max(ans, cnt)

    fish(sh_r, sh_c, arr)

    for i in range(1, 5):
        sh_ni, sh_nj = sh_r + move[sh_dir][0] * i, sh_c + move[sh_dir][1] * i
        if 0 <= sh_ni < 4 and 0 <= sh_nj < 4 and arr[sh_ni][sh_nj][0] != 0:
            shark(sh_ni, sh_nj, cnt + arr[sh_ni][sh_nj][0], copy.deepcopy(arr))


shark(0, 0, arr[0][0][0], arr)
print(ans)

