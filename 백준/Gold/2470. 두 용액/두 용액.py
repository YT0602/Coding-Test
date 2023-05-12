N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()
s = 0
e = N-1
ans = 2_000_000_000
mn = mx = 0
while s < e:
    result = liquid[s] + liquid[e]
    if abs(result) < ans:
        ans = abs(result)
        mn = liquid[s]
        mx = liquid[e]
        if ans == 0:
            break
    if result < 0:
        s += 1
    else:
        e -= 1
print(mn, mx)

