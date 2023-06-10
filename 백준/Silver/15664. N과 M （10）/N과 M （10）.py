def back(start):
    global last
    last = 0
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, N):
        if not visit[i] and numbers[i] != last:
            visit[i] = True
            lst.append(numbers[i])
            back(i+1)
            visit[i] = False
            last = lst.pop()


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visit = [False] * N
lst = []
last = 0
back(0)