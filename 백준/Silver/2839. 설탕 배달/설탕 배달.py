import sys

input = sys.stdin.readline

count = 0
N = int(input())
while N > 0:
    if N % 5 == 0:  # 5로 나누어 떨어지면 횟수에 몫만큼 추가
        count += N // 5
        N = 0  # N = 0되고 반복 종료
        break
    else:  # 나누어 떨어지지 않으면 3빼고 횟수 1 증가
        N -= 3
        count += 1
if N == 0:
    print(count)
else:  # 0 미만으로 나오면 -1 출력
    print(-1)
