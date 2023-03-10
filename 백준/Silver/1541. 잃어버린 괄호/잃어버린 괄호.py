num = ''
cal = []
numbers = []
for i in input():
    if i.isdigit():
        num += i
    else:
        cal.append(i)
        numbers.append(int(num))
        num = ''
numbers.append(int(num))

result = []
tmp = numbers[0]
for i in range(len(cal)):
    if cal[i] == '-':
        result.append(tmp)
        tmp = numbers[i+1]

    else:
        tmp += numbers[i+1]

result.append(tmp)
ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]

print(ans)