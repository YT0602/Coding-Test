import sys
input = sys.stdin.readline

K = int(input())
row = 0
row_idx = 0
col = 0
col_idx = 0
no_ground = []
road = [list(map(int, input().split())) for i in range(6)]

# 가로, 세로 나눠서 추가
for i in range(6):
    if road[i][0] == 1 or road[i][0] == 2:
        if row < road[i][1]:
            row = road[i][1]
            row_idx = i
    else:
        if col < road[i][1]:
            col = road[i][1]
            col_idx = i
# print(row, row_idx)
# print(col, col_idx)
# print(road)
if row_idx != 5:
    no_row = abs(road[row_idx-1][1] - road[row_idx+1][1])
else:
    no_row = abs(road[row_idx - 1][1] - road[0][1])

if col_idx != 5:
    no_col = abs(road[col_idx-1][1] - road[col_idx+1][1])
else:
    no_col = abs(road[col_idx - 1][1] - road[0][1])
# print(no_row, no_col)

# 전체 넓이 = (가로 최대 x 세로 최대) - (땅따먹기 구역)
area = row*col - (no_row * no_col)
print(area*K)