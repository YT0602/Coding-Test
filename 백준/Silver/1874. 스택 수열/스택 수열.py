import sys
input = sys.stdin.readline

N = int(input())
stk = []  # 숫자 스택
result = []  # 부호 리스트
count = 1
for test in range(N):  # 입력받아서 스택에 추가
    num = int(input())
    while count <= num:  # count가 입력숫자 될때까지
        stk.append(count)  # stk에 숫자 추가, result에 부호 추가, count 1증가
        result.append('+')
        count += 1
    # 수정부분
    if stk[-1] == num:  # stk 마지막 원소가 입력숫자와 같으면 pop하고 -추가
        stk.pop()
        result.append('-')
    else:  # 아니면 종료
        break
if len(stk) == 0:  # stk이 모두 비워졌으면 부호 하나씩 프린트, 아니면 NO
    for i in result:
        print(i)
else:
    print('NO')