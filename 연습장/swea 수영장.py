# def DFS(num, sm):
#     global ans
#     if sm >= ans:
#         return
#
#     if num > 12:
#         ans = min(sm, ans)
#         return
#
#     DFS(num + 1, sm + day*swim[num])  # 일일권
#     DFS(num + 1, sm + mon)  # 월간권
#     DFS(num + 3, sm + mon3)  # 분기권
#     DFS(num + 12, sm + year)    # 연간권


T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))
    # 백트래킹
    # ans = 365*3000
    # DFS(1, 0)

    # 규칙 찾기
    s = [0] * 13
    for i in range(1, 13):
        # i달까지의 최소비용
        s[i] = s[i-1] + day * swim[i]  # 일일권
        s[i] = min(s[i], s[i-1] + mon)  # 월간권
        if i >= 3:
            s[i] = min(s[i], s[i - 3] + mon3)  # 분기권
        if i >= 12:
            s[i] = min(s[i], s[i-12] + year)  # 연간권

    ans = s[12]

    print(f'#{tc} {ans}')