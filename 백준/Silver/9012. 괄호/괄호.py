import sys
input = sys.stdin.readline

T = int(input())
for test in range(T):
    VPS = input()
    stk = []  # 빈 스택
    for i in VPS:
        if i == '(':  # 원소가 '('면 스택에 추가
            stk.append(i)
        elif i == ')':  # 원소가 ')'일 때
            if len(stk) == 0:  # 스택이 비어있으면 추가하고 해당 입력 종료
                stk.append(i)
                break
            else:  # 스택이 비어있지 않으면 맨 뒤의 원소 삭제
                stk.pop()
    if len(stk) == 0:  # 문자열 끝난뒤에 스택이 비어있으면 YES
        print('YES')
    else:  # 아니면 NO
        print('NO')
