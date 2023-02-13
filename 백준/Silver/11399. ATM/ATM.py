import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
ans = 0
# for i in range(N-1):
#     mn_idx = i
#     for j in range(i+1, N):
#         if time[mn_idx] > time[j]:
#             mn_idx = j
#         time[i], time[mn_idx] = time[mn_idx], time[i]
time.sort()
for i in range(N):
    ans += sum(time[:i+1])
print(ans)