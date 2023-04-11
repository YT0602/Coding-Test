import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
LIS = [numbers[0]]


# 이분탐색
def bisect(num):
    s = 0
    e = len(LIS)-1

    while s <= e:
        mid = (s+e)//2

        if LIS[mid] == num:
            return mid
        elif LIS[mid] < num:
            s = mid + 1
        elif LIS[mid] > num:
            e = mid - 1
    return s


for i in range(1, N):
    # 원소가 배열 마지막 수보다 크면 바로 추가
    if LIS[-1] < numbers[i]:
        LIS.append(numbers[i])
    # 마지막 수보다 작으면 들어갈 자리 이분탐색으로 찾기
    else:
        idx = bisect(numbers[i])
        LIS[idx] = numbers[i]

print(len(LIS))