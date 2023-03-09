N = input()
bomb = input()
x = len(bomb)
ans = []
for i in N:
    ans.append(i)
    if len(ans) >= x:
        if ''.join(ans[-x:]) == bomb:
            for j in range(x):
                ans.pop()

if len(ans):
    print(''.join(ans))
else:
    print('FRULA')