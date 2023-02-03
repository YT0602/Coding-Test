for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump > 0:  # 정렬 후 맨 끝 -1, 맨 앞 +1, 횟수 -1
        box.sort()
        box[0] += 1
        box[-1] -= 1
        dump -= 1

    box.sort()  # 마지막에 한번 더 정렬
    x = box[-1] - box[0]  # 최대 - 최소
    print(f'#{tc} {x}')
