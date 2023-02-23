import sys
input = sys.stdin.readline


def back():
    global last
    last = 0
    if len(lst) == M+1:
        print(*lst[1:])
        return
    for i in range(N):
        if numbers[i] >= lst[len(lst)-1] and numbers[i] != last:
            lst.append(numbers[i])
            back()
            last = lst.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
lst = [0]
last = 0
back()