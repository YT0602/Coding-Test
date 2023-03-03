L = int(input())
N = int(input())
people = []
# 희망 길이 리스트
hope = []
# 번호 적을 롤 케잌 리스트
cake = [0]*(L+1)

for i in range(N):
    P, K = map(int, input().split())
    people.append([P, K])
    hope.append(K-P)
    # 번호 안적혀있으면 번호적기
    for j in range(P, K+1):
        if cake[j] == 0:
            cake[j] = i+1

# 가장 기대하던 참가자
print(hope.index(max(hope))+1)

# 가장 많이 받은 참가자
most = [0] * N
for i in cake:
    if i != 0:
        most[i-1] += 1
print(most.index(max(most))+1)