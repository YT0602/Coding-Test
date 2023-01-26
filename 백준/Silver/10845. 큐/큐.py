import sys
from collections import deque

N = int(sys.stdin.readline())
st = deque()
for _ in range(N):
    name = list(sys.stdin.readline().split())  # 입력 리스트로 변경
    if name[0] == 'push':  # 명령이 push면
        st.append(int(name[1]))  # 덱에 숫자 추가
    if name[0] == 'pop':  # 명령이 pop이면 원소가 없으면 -1, 아니면 맨 앞 원소 빼내기
        if len(st) == 0:
            print(-1)
        else:
            print(st.popleft())
    if name[0] == 'size':  # 명령이 size면 원소개수 출력
        print(len(st))
    if name[0] == 'empty':  # 명령이 empty면 원소가 없으면 1, 아니면 0 출력
        if len(st) == 0:
            print(1)
        else:
            print(0)
    if name[0] == 'front':  # 명령이 front면 원소가 없으면 -1, 있으면 맨 앞의 원소 출력
        if len(st) == 0:
            print(-1)
        else:
            print(st[0])
    if name[0] == 'back':  # 명령이 back이면 원소가 없으면 -1, 있으면 맨 뒤의 원소 출력
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])