T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 작업 시간 리스트
    work = []
    # 가능한 화물차 개수
    cnt = 0
    # 시작시간, 끝시간 추가
    for i in range(N):
        s, e = map(int, input().split())
        work.append([s, e])
    # 끝나는 시간 기준으로 정렬
    work.sort(key=lambda x: x[1])
    # 현재 시간
    cur = 0
    for i in range(N):
        # 시작시간이 현재시간보다 뒤면 카운트
        if work[i][0] >= cur:
            cnt += 1
            # 현재시간 갱신
            cur = work[i][1]
    print(f'#{tc} {cnt}')

