while True:
    N = list(map(int, input()))
    if N == N[::-1]:
        if N[0] == 0:
            break
        print('yes')
    else:
        print('no')