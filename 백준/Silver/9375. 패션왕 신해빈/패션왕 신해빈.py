T = int(input())
for tc in range(T):
    N = int(input())
    clothes = [input().split() for _ in range(N)]
    wear = {}
    cnt = []  # 종류별 개수
    result = 1  # 입을수 있는 종류
    for i in clothes:
        wear.setdefault(i[1], [])
        wear[i[1]] += [i[0]]
    for j in wear:
        cnt.append(len(wear[j]))
    for j in cnt:
        result *= j+1  # 공집합 포함 1개 뽑는 경우의 수 

    print(result-1)  # 공집합인 경우 제외