T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    come = list(map(int, input().split()))
    come.sort()
    # 도착시간 간격 리스트
    come_new = [come[0]]
    for i in range(1, N):
        come_new.append(come[i]-come[i-1])
    make = 0
    ans = 'Possible'
    t = 0
    for i in range(N):
        make += ((come_new[i] + t) // M)*K
        t = (come_new[i] + t) % M
        if make == 0 and come_new[i] < M:
            ans = 'Impossible'
            break
        else:
            make -= 1
    print(f'#{tc} {ans}')
    # print(come_new)