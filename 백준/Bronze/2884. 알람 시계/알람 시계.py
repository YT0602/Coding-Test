H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H1 = 23
    else:
        H1 = H -1
    M1 =(60 - 45+M)
else:
    H1 = H
    M1 = M-45

print(H1, M1)