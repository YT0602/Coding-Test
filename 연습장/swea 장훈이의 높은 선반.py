def tower(num, sm):
    global mn
    if sm > mn:
        return
    # N까지 왔을때 B이상이면 최소 비교
    if num == N:
        if sm >= B:
            mn = min(sm, mn)
        return

    # num번째 수를 포함하는 경우
    tower(num+1, sm+H[num])
    # 포함하지 않는 경우
    tower(num+1, sm)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    mn = 200000
    tower(0, 0)
    print(f'#{tc} {mn-B}')