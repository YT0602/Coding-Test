def calcul(n, ans):
    global mx, mn
    if n == N-1:
        mx = max(mx, ans)
        mn = min(mn, ans)
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            if i == 0:
                calcul(n+1, ans + numbers[n+1])
            elif i == 1:
                calcul(n + 1, ans - numbers[n + 1])
            elif i == 2:
                calcul(n + 1, ans * numbers[n + 1])
            elif i == 3:
                if ans < 0:
                    ans = -((-ans)//numbers[n+1])
                    calcul(n + 1, ans)
                else:
                    calcul(n+1, ans // numbers[n+1])
            cal[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))

mx = -1000000000
mn = 1000000000

calcul(0, numbers[0])
print(mx)
print(mn)
