def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                stack.append(i)
                break
            if stack.pop() != "(":
                break
    if stack:
        answer = False
    
    return answer