L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()
password = ''
v = [0] * C
mo = ['a', 'e', 'i', 'o', 'u']


def solve(idx, password):
    if len(password) == L:
        x = y = 0
        for st in password:
            if st in mo:
                x += 1
            else:
                y += 1
        if x >= 1 and y >= 2:
            print(password)
        return

    for i in range(idx, C):
        if v[i] == 0:
            v[i] = 1
            solve(i+1, password + alpha[i])
            v[i] = 0


solve(0, password)