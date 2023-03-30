def cost(num, cnt):
    global mn_cnt
    # N행까지 왔으면 최솟값 비교
    if num == N:
        mn_cnt = min(cnt, mn_cnt)
        return
    # 중간에 최솟값보다 값이 커지면 중단
    if cnt > mn_cnt:
        return
    for i in range(N):
        # 아직 생산하지 않는 공장이면 선택하고 재귀
        if v[i] == 0:
            v[i] = 1
            cost(num+1, cnt + arr[num][i])
            v[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방문 체크
    v = [0] * N
    mn_cnt = 9999
    cost(0, 0)
    print(f'#{tc} {mn_cnt}')