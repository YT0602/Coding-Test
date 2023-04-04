def solution(k, tangerine):
    ans = 0
    numbers = dict()
    # 크기별 개수 정리
    for i in tangerine:
        numbers.setdefault(i, 0)
        numbers[i] += 1
    # 개수 많은 순으로 정렬
    new = sorted(numbers.items(), key=lambda x: x[1], reverse=True)
    # 종류 수
    cnt = 0
    # 필요한 개수 이상되면 종료
    for i in new:
        cnt += i[1]
        ans += 1
        if cnt >= k:
            break
    return ans
