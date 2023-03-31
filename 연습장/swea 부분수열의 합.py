def comb(num, idx, list):
    global cnt
    # 부분집합 합이 K면 정답처리하고 반환
    if idx == N:
        if list == num:
            cnt += 1
        return
    # 중간에 합이 K보다 커지면 중단
    if list > num:
        return

    # 마지막에 탐색한 인덱스 다음부터 시작
    comb(num, idx+1, list + numbers[idx])
    comb(num, idx + 1, list)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 방문체크
    v = [0] * N
    # 정답 수
    cnt = 0
    # 부분집합
    result = []

    comb(K, 0, 0)

    print(f'#{tc} {cnt}')
