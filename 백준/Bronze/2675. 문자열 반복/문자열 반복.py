T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    for i in range(len(S)):
        a = S[i] * R
        print(a, end='')
    print()