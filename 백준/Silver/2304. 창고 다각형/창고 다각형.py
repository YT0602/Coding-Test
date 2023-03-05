N = int(input())
lst = [0] * 1001
mx_i = mx = 0
for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H
    # mx_i 구하기
    if mx < H:
        mx_i, mx = L, H

# 왼쪽부터 처리
ans = mx = 0
for i in range(mx_i+1):
    mx = max(mx, lst[i])
    ans += mx

# 오른쪽부터 처리
mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, lst[i])
    ans += mx
print(ans)