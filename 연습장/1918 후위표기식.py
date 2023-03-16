
solve = input()
calcul = []

for i in solve:
    # 알파벳이면 그대로 출력
    if i.isalpha():
        print(i, end='')
    else:
        # 여는 괄호면 push
        if i == '(':
            calcul.append(i)
        # 닫는 괄호면 여는괄호 나올때 까지 pop해서 출력
        elif i == ')':
            while len(calcul) != 0 and calcul[-1] != '(':
                print(calcul.pop(), end='')
            # 여는괄호 제거
            calcul.pop()
        # 곱셈 나눗셈이면
        elif i == '*' or i == '/':
            if calcul:
                # top이 우선순위가 더 낮으면 push
                if calcul[-1] == '(' or calcul[-1] == '+' or calcul[-1] == '-':
                    calcul.append(i)
                # 우선순위가 같거나 높으면 낮은거 나올때까지 pop해서 출력하고 push
                else:
                    while calcul[-1] == '*' or calcul[-1] == '/':
                        print(calcul.pop(), end='')
                        if len(calcul) == 0:
                            break
                    calcul.append(i)
            else:
                calcul.append(i)
        elif i == '+' or i == '-':
            if calcul:
                if calcul[-1] == '(':
                    calcul.append(i)
                else:
                    while len(calcul) != 0 and calcul[-1] != '(':
                        print(calcul.pop(), end='')
                    calcul.append(i)
            else:
                calcul.append(i)
# 남은거 출력
while calcul:
    print(calcul.pop(), end='')
