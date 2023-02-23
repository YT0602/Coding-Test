import sys
input = sys.stdin.readline


def back():
    global last
    last = 0
    if len(lst) == M:
        # if ''.join(map(str, lst)) in ans:
        #     return
        print(*lst)
        # ans.append(''.join(map(str, lst)))
        return
    for i in range(N):

        if numbers[i] != last and visited[i] == 0:
            lst.append(numbers[i])
            visited[i] = 1
            back()
            last = numbers[i]
            lst.pop()
            visited[i] = 0


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [0] * N
lst = []
last = 0
back()