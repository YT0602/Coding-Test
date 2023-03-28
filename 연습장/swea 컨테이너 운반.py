T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 트럭별 실은 화물 무게
    work = [0] * M
    idx = 0
    # 트럭 인덱스, 화물 인덱스
    T_num = 0
    C_num = 0

    while container and truck:
        mx_T = max(truck)
        mx_C = max(container)
        # 적재가능량이 더 크면 트럭에 넣고 제거
        if mx_T >= mx_C:
            work[idx] = mx_C
            idx += 1
            container.remove(mx_C)
            truck.remove(mx_T)

        # 화물무게가 더 크면 화물 제거
        elif mx_T < mx_C:
            container.remove(mx_C)

    print(f'#{tc} {sum(work)}')