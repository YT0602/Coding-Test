# num개의 원소를 가진 부분 집합 구하기
def comb(list, num):
    result = []
    if num > len(list):
        return result

    if num == 1:
        for i in list:
            result.append([i])

    elif num > 1:
        for i in range(len(list) - num + 1):
            for j in comb(list[i+1:], num-1):
                result.append([list[i]] + j)
    return result


# 각 리스트에서 두개씩 골라 시너지 합산
def cook(list1, list2, sm1, sm2):
    for r, c in comb(list1, 2):
        sm1 += (arr[r][c]+arr[c][r])
    for r, c in comb(list2, 2):
        sm2 += (arr[r][c]+arr[c][r])
    return abs(sm1 - sm2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    ans = 9999

    for food in comb(range(N), N//2):
        # 중복되지 않는 재료 리스트
        another = list(set(range(N)) - set(food))
        cnt = cook(food, another, 0, 0)
        ans = min(ans, cnt)

    print(f'#{tc} {ans}')