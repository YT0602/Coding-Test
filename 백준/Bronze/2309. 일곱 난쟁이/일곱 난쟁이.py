import sys
from itertools import combinations

input = sys.stdin.readline

nan = []
for i in range(9):  # 난쟁이들 키 추가
    height = int(input())
    nan.append(height)

nan.sort()  # 오름차순 정렬
result = list(combinations(nan, 7))  # 7명씩 조합 경우의 수
for j in result:  # 경우의 수 중에 합이 100이면 하나씩 출력
    if sum(j) == 100:
        for k in j:
            print(k)
        break