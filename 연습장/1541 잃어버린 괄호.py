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

result = [numbers[0]]
ans = 0
if len(cal) == 1:
    if cal[0] == '+':
        print(numbers[0]+numbers[1])
    else:
        print(numbers[0]-numbers[1])
else:
    for i in range(len(cal)):
        if cal[i] == '-':

            for j in range(len(result)):
                ans += result.pop(0)
            result.append(ans)
            ans = 0
            result.append('-')
            result.append(numbers[i + 1])

        else:
            result.append(numbers[i+1])


print(cal)
print(numbers)
print(result)