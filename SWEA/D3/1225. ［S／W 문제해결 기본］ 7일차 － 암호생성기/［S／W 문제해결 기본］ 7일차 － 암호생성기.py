from collections import deque

for tc in range(1, 11):
    T = int(input())
    numbers = deque(map(int, input().split()))
    cnt = 0
    sub = [1, 2, 3, 4, 5]
    y = 10000
    while y > 0:
        x = numbers.popleft()
        y = x - sub[cnt % 5]
        numbers.append(y)
        cnt += 1
    numbers[-1] = 0
    print(f'#{tc}', *numbers)