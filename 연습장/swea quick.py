def quick(list, l, r):
    s = l
    e = r
    pivot = list[(s + e) // 2]
    while s <= e:
        # 피벗보다 작으면 계속 진행
        while list[s] < pivot:
            s += 1
        # 피벗보다 크면 계속 진행
        while list[e] > pivot:
            e -= 1
        # 왼쪽은 피벗보다 크고 오른쪽은 작을 때, 포인터가 교차하지 않았다면 교환
        if s <= e:
            list[s], list[e] = list[e], list[s]
            s += 1
            e -= 1
    # 왼쪽 그룹 재귀로 퀵정렬
    if l < e: quick(list, l, e)
    # 오른쪽그룹
    if s < r: quick(list, s, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick(numbers, 0, len(numbers) - 1)

    print(f'#{tc} {numbers[N//2]}')