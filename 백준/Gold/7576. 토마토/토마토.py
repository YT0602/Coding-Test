import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
box = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0

def tomato():
  while box:
    cx, cy = box.popleft()
    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if 0 <= nx < row and 0 <= ny < col and arr[nx][ny] == 0:
        arr[nx][ny] = arr[cx][cy] + 1
        box.append((nx, ny))

def check():
  global day
  for i in arr:
    for j in range(col):
      if i[j] == 0:
        return -1
      elif i[j] > day:
        day = i[j]
  return day - 1

for i in range(row):
  for j in range(col):
    if arr[i][j] == 1:
      box.append((i, j))
tomato()

print(check())
