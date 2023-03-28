def triplet(list):
    # 3장 이상인 카드 있다면 True
    if list.count(3) >= 1:
        return True


def is_run(list):
    cnt = 0
    for i in list:
        # 카드가 3장 연속 있다면 True
        if i != 0:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    # 숫자별 카드 개수 리스트
    p1 = [0] * 10
    p2 = [0] * 10
    # 승자 번호
    ans = 0
    for i in range(len(numbers)):
        # 홀수번째는 p1에 넣고 run, triplet 판단
        if i % 2 == 0:
            p1[numbers[i]] += 1
            if triplet(p1) or is_run(p1):
                ans = 1
                break
        # 짝수번째는 p2에 넣고 run, triplet 판단
        else:
            p2[numbers[i]] += 1
            if triplet(p2) or is_run(p2):
                ans = 2
                break

    print(f'#{tc} {ans}')