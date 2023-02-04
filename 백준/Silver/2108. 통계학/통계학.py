import sys
from collections import Counter
input = sys.stdin.readline


def avg(list):  # 산술평균
    x = sum(list)/N  # 합/개수
    return int(round(x, 0))  # 반올림


def mid(list):  # 중앙값
    list.sort()
    return list[N//2]


def most(list):  # 최빈값
    cnt = Counter(list).most_common(2)  # Counter 모듈로 빈도수 딕셔너리 생성 후 상위 2개
    if N > 2:  # 원소 두개 이상일때
        if cnt[0][1] == cnt[1][1]:  # 상위 두개의 빈도 수가 같으면 두번째 키 반환
            return cnt[1][0]
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]


def rng(list):  # 범위
    return max(list) - min(list)


N = int(input())
numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

print(avg(numbers))
print(mid(numbers))
print(most(numbers))
print(rng(numbers))