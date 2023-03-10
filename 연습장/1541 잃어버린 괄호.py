num = ''
cal = []
numbers = []

# 연산자와 숫자 분리
for i in input():
    if i.isdigit():
        num += i
    else:
        cal.append(i)
        numbers.append(int(num))
        num = ''
numbers.append(int(num))

# + 연산만 실행해서 리스트에 추가, - 연산이면 그냥 추가
result = []
tmp = numbers[0]
for i in range(len(cal)):
    if cal[i] == '-':
        result.append(tmp)
        tmp = numbers[i+1]

    else:
        tmp += numbers[i+1]

# - 연산 실행
result.append(tmp)
ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]

print(ans)