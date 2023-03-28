def elec(num, x, cnt):
    global mn_cnt
    # 깊이 N까지 왔으면 최솟값 갱신
    if num == N:
        mn_cnt = min(mn_cnt, cnt)
        return
    # 깊이 N-1일때는 시작시점으로 돌아가야함
    elif num == N-1:
        elec(num+1, x, cnt + arr[x][0])
    else:
        for i in range(1, N):
            cur = i
            # 이전위치와 현재위치가 다르고 방문하지 않은 곳이면 값 추가하고 재귀 호출
            if cur != x and cur not in visit:
                visit.add(cur)
                elec(num+1, cur, cnt + arr[x][cur])
                visit.remove(cur)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    mn_cnt = 5000
    # 방문 확인 리스트
    visit = set()

    for j in range(1, N):
        cnt = 0
        # 시작은 무조건 0
        # 방문처리 후 재귀호출
        visit.add(j)
        elec(1, j, arr[0][j])
        # 돌아오면 방문처리 해제하고 값 다시 빼기
        visit.remove(j)

    print(f'#{tc} {mn_cnt}')