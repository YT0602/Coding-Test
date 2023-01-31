while True:
    words = list(input())
    stk = []
    if words == ['.']:
        break
    for i in words:
        if '(' in i:
            stk.append('(')
        if '[' in i:
            stk.append('[')
        if ')' in i:
            if len(stk) == 0 or stk.pop() == '[':
                stk.append(')')
                break
        if ']' in i:
            if len(stk) == 0 or stk.pop() == '(':
                stk.append(']')
                break
    if len(stk) == 0:
        print('yes')
    else:
        print('no')
