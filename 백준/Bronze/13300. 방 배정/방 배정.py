import sys
from collections import Counter
input = sys.stdin.readline

N, K = map(int, input().split())
boy = []
girl =[]
cnt = 0
for i in range(N):
    S, Y = map(int, input().split())
    if S:
        boy.append(Y)
    else:
        girl.append(Y)

boy_dict = Counter(boy)
girl_dict = Counter(girl)
# print(boy_dict)
# print(girl_dict)
for j in boy_dict.values():
    if j == 0:
        continue
    elif j % K == 0:
        cnt += (j // K)
    else:
        cnt += ((j // K) + 1)

for j in girl_dict.values():
    if j == 0:
        continue
    elif j % K == 0:
        cnt += (j // K)
    else:
        cnt += ((j // K) + 1)
print(cnt)