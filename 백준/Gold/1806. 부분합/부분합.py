N, S = map(int, input().split())
numbers = list(map(int, input().split()))

s = 0
e = 0
sm = numbers[0]
ans = N+1
while e < N:
    if sm >= S:
        ans = min(e-s+1, ans)
        sm -= numbers[s]
        s += 1
    else:
        e += 1
        if e == N:
            break
        sm += numbers[e]
        
if ans > N:
    print(0)
else:
    print(ans)