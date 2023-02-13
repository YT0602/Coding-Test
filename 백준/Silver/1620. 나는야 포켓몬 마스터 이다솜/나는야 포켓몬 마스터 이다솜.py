import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dogam = dict()
for i in range(N):
    pkmon = input().strip()
    dogam[str(i+1)] = pkmon
    dogam[pkmon] = i+1
for j in range(M):
    search = input().strip()
    print(dogam[search])