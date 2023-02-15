import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum_s = 0
# 구간 합 리스트, 시작이 1일때는 뺄게 없으므로 맨 앞에 0 추가
area_sum = [0]
# 각 인덱스까지의 합을 리스트에 추가
for i in numbers:
    sum_s += i
    area_sum.append(sum_s)
    
for i in range(M):
    S, E = map(int, input().split())
    print(area_sum[E] - area_sum[S-1])