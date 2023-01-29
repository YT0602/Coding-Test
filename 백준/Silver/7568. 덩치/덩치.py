import sys
input = sys.stdin.readline

T = int(input())
people = []  # 키, 몸무게 저장 리스트
for test in range(T):
    body = tuple(map(int, input().split()))  
    people.append(body)  # (키, 몸무게) 형식으로 추가
rank_list = []
for i in range(len(people)):  
    rank = 1
    for j in range(len(people)):  # 키, 몸무게 모두 더 큰 원소 있으면 현재 원소 rank + 1
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    rank_list.append(rank)
print(*rank_list)