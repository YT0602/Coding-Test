from collections import deque
import sys
input = sys.stdin.readline


def BFS(row, col):
    land = deque()
    land.append((row, col))
    arr[row][col] = 0
    move = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    
    while land:
        r, c = land.popleft()
        
        for x in range(8):
            nr, nc = r + move[x][0], c + move[x][1]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == 1:
                    land.append((nr, nc))
                    arr[nr][nc] = 0


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                BFS(i, j)
                ans += 1

    print(ans)
