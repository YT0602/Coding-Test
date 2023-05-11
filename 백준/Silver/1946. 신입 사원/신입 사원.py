T = int(input())
for _ in range(T):
    N = int(input())
    people = []

    for i in range(N):
        paper, interview = map(int, input().split())
        people.append((paper, interview))

    people.sort()

    top = people[0][1]
    cnt = 1
    for i in range(1, N):
        if people[i][1] < top:
            top = people[i][1]
            cnt += 1
    print(cnt)