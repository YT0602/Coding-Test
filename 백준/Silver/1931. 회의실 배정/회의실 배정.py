import sys

input = sys.stdin.readline

N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
# 끝나는 시간 기준 오름차순 정렬 후 시작시간 기준 오름차순 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
cnt = 1
# 맨 처음 회의 끝나는 시간
last = meeting[0][1]

for i in range(1, N):
    # 앞 회의 끝난 시간 뒤에 회의 시작이면 추가하고 끝나는 시간 갱신
    if meeting[i][0] >= last:
        cnt += 1
        last = meeting[i][1]

print(cnt)