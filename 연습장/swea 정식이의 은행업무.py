def change(num, cnt):
    x = len(num)-1
    result = 0
    for i in num:
        result += int(i)*cnt**x
        x -= 1
    return result


T = int(input())
for tc in range(1, T+1):
    num2 = input()
    num3 = input()

    ans = 0
    x2 = change(num2, 2)
    x3 = change(num3, 3)

    sub = abs(x2 - x3)
    mul2 = len(num2) - 1
    while (sub - 2**mul2) % 3 != 0:
        mul2 -= 1

    ans = x2 + 2**mul2
    print(f'#{tc} {ans}')

