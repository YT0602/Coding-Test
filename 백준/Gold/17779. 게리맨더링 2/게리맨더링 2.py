N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in arr:
    total += sum(i)

ans = 100*20*20


def DFS(r, c, d1, d2, arr):
    # 5선거구
    # 경계선
    v = [[0] * N for _ in range(N)]
    v[r][c] = 5
    for i in range(1, d1+1):
        v[r+i][c-i] = 5
        v[r+d2+i][c+d2-i] = 5
    for i in range(1, d2+1):
        v[r+i][c+i] = 5
        v[r+d1+i][c-d1+i] = 5

    people = [0] * 5
    # 1선거구
    for i in range(r+d1):
        for j in range(c+1):
            if v[i][j] == 5:
                break
            people[0] += arr[i][j]

    # 2선거구
    for i in range(r+d2+1):
        for j in range(N-1, c, -1):
            if v[i][j] == 5:
                break
            people[1] += arr[i][j]

    # 3선거구
    for i in range(r+d1, N):
        for j in range(c-d1+d2):
            if v[i][j] == 5:
                break
            people[2] += arr[i][j]

    # 4선거구
    for i in range(r + d2+1, N):
        for j in range(N-1, c-d1+d2-1, -1):
            if v[i][j] == 5:
                break
            people[3] += arr[i][j]

    people[4] = total - sum(people)
    result = max(people) - min(people)
    return result


for i in range(N-2):
    for j in range(1, N-1):
        for k in range(1, N-1):
            for l in range(1, N-1):
                if 0 <= j - k and j+l < N and i + k + l < N:
                    ans = min(DFS(i, j, k, l, arr), ans)
print(ans)