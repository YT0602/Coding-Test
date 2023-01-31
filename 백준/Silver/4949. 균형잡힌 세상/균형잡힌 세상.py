import sys
input = sys.stdin.readline

while True:
    words = list(input().rstrip())
    stk = []
    if words == ['.']:  # . 입력되면 종료
        break
    for i in words:
        if '(' in i:  # ( or [ 면 스택에 추가
            stk.append('(')
        if '[' in i:
            stk.append('[')
        if ')' in i:  # 원소가 ), ] 일때 스택이 비어있거나 pop한 원소가 [, ( 면 해당 원소 추가하고 종료
            if len(stk) == 0 or stk.pop() == '[':
                stk.append(')')
                break
        if ']' in i:
            if len(stk) == 0 or stk.pop() == '(':
                stk.append(']')
                break
    if len(stk) == 0:  # 스택이 비어있으면 yes 아니면 no
        print('yes')
    else:
        print('no')
