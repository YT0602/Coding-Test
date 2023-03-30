def binary(l, r, target, dir):
    global cnt
    mid = (l+r)//2
    if l > r:
        return
    if A[mid] == target:
        cnt += 1
        return
    # 중앙값이 타겟보다 작을 때
    elif A[mid] < target:
        # 이전 탐색 구간이 오른쪽이면 중단
        if dir == 1:
            return
        # 이전 탐색 구간이 왼쪽이면 재귀
        else:
            binary(mid+1, r, target, 1)
    # 중앙값이 타겟보다 클 때
    else:
        # 이전 탐색 구간이 왼쪽이면 중단
        if dir == 0:
            return
        # 이전 탐색 구간이 오른쪽이면 재귀
        else:
            binary(l, mid-1, target, 0)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0

    for i in B:
        binary(0, len(A)-1, i, -1)

    print(f'#{tc} {cnt}')