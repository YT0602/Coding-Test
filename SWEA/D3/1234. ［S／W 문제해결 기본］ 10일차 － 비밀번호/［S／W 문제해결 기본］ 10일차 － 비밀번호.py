for tc in range(1, 11):
    N, password = input().split()
    num = list(password)
    stack = []
    for i in num:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(f"#{tc} {''.join(stack)}")