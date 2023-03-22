import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
s = 0
e = N - 1
ans = 2000000000
num1 = 0
num2 = 0
# 두 포인터가 교차하기 전까지 진행
while s < e:
    if abs(numbers[s] + numbers[e]) == 0:
        ans = 0
        num1 = numbers[s]
        num2 = numbers[e]
        break
    # 절댓값이 더 작으면 갱신
    elif abs(numbers[s] + numbers[e]) < abs(ans):
        num1 = numbers[s]
        num2 = numbers[e]
        ans = numbers[s] + numbers[e]
        # 두 수의 합이 0보다 크면 뒤쪽 포인터 당김
        if numbers[s] + numbers[e] > 0:
            e -= 1
        # 0보다 작으면 앞쪽 포인터 당김
        else:
            s += 1
    elif abs(numbers[s] + numbers[e]) >= abs(ans):
        if numbers[s] + numbers[e] > 0:
            e -= 1
        else:
            s += 1

# print(ans)
print(num1, num2)
