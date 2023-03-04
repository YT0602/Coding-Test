arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자
call = []
for i in range(5):
    call += list(map(int, input().split()))
# 번호마다 좌표의 위치 저장
pos = [0] * 26
for i in range(5):
    for j in range(5):
        pos[arr[i][j]] = (i, j)

v = [[0] * 10 for _ in range(4)]  # 가로, 세로, 대각, 빈도수 체크

# 사회자가 부르는 좌표 읽어서, 빈도수 체크, 5가 3개 이상이면 종료
for n in call:
    i, j = pos[n]  # 번호에서 좌표 읽어오기
    v[0][j] += 1  # 세로 개수 누적
    v[1][i] += 1  # 가로 개수 누적
    v[2][i - j] += 1  # 우하향 대각선 개수 누적
    v[3][i + j] += 1  # 우상향 대각선 개수 누적
    cnt = 0
    for t in v:
        cnt += t.count(5)  # 한줄 완성된 개수
    if cnt >= 3:
        break
print(sum(v[0]))  # 표시된 개수가 불러준 숫자의 개수
