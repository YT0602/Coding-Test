import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().strip().split()))
M = int(input())
cards_M = list(map(int, input().strip().split()))

dict_N = Counter(cards)
# Counter 모듈 활용하여 cards 리스트에서 {해당 숫자 : 개수} 행태로 딕셔너리 생성
count_list = []
for i in cards_M:  # M 리스트 돌면서 그 숫자의 value값 추가
    count_list.append(dict_N[i])

print(*count_list)
