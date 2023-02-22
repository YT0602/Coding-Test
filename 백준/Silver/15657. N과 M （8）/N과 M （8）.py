import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
lst = []
numbers.sort()


def back():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(N):
        if numbers[i] >= lst[len(lst)-1]:
            lst.append(numbers[i])
            back()
            lst.pop()


for j in range(len(numbers)):
    lst.append(numbers[j])
    back()
    lst.pop()

