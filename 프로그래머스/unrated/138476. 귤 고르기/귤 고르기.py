def solution(k, tangerine):
    ans = 0
    numbers = dict()
    
    for i in tangerine:
        numbers.setdefault(i, 0)
        numbers[i] += 1
    new = sorted(numbers.items(), key=lambda x: x[1], reverse=True)

    cnt = 0
    for i in new:
        cnt += i[1]
        ans += 1
        if cnt >= k:
            break
    return ans