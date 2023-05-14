import sys
sys.setrecursionlimit(10**5)


def project(num):
    global ans
    v[num] = True
    team.append(num)
    next = choice[num]

    if v[next]:
        # 사이클 돌면 사이클 시작 구간 부터 팀 구성
        if next in team:
            ans += team[team.index(next):]
        return
    # 사이클 아니면 재귀
    else:
        project(next)


T = int(input())
for _ in range(T):
    N = int(input())
    choice = [0] + list(map(int, input().split()))
    v = [False] * (N+1)
    ans = []

    for i in range(1, N+1):
        if not v[i]:
            team = []
            project(i)
    # 전체 - 팀 이룬 사람 수
    print(N-len(ans))