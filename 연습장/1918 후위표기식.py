
solve = input()
calcul = []

for i in solve:
    if i.isalpha():
        print(i, end='')
    else:
        if i == '(':
            calcul.append(i)
        elif i == ')':
            while len(calcul) != 0 and calcul[-1] != '(':
                print(calcul.pop(), end='')
            calcul.pop()
        elif i == '*' or i == '/':
            if calcul:
                if calcul[-1] == '(' or calcul[-1] == '+' or calcul[-1] == '-':
                    calcul.append(i)
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
while calcul:
    print(calcul.pop(), end='')
