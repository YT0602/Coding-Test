def DFS(num, sm):
    global ans
    if sm >= ans:
        return

    if num > 12:
        ans = min(sm, ans)
        return

    DFS(num + 1, sm + day*swim[num])  # 일일권
    DFS(num + 1, sm + mon)  # 월간권
    DFS(num + 3, sm + mon3)  # 분기권
    DFS(num + 12, sm + year)    # 연간권


T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))

    ans = 365*3000

    DFS(1, 0)

    print(f'#{tc} {ans}')