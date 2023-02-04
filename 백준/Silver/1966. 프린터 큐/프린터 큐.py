import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    num = deque(list(map(int, input().split())))
    cnt = 0
    while M != -1:
        if num[0] != max(num):  # 맨 앞 원소가 최대가 아니면 맨 뒤로
            num.append(num.popleft())
            if M == 0:  # 이때 M 이 맨 앞이면 인덱스를 맨 끝으로 변경
                M = len(num) -1
            else:  # 아니면 한 칸 앞으로
                M -= 1
        else:  # 최대 숫자면 pop
            num.popleft()
            M -= 1
            cnt += 1
    print(cnt)