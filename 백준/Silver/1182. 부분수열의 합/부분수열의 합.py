import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
cnt = 0
result = []


def set_sum(num, target, idx):
    global cnt
    if len(result) > 0 and sum(result) == target:
        cnt += 1

    elif idx >= num:
        return
    for i in range(idx, num):
        result.append(numbers[i])
        set_sum(num, target, i+1)
        result.pop()


set_sum(N, S, 0)
print(cnt)