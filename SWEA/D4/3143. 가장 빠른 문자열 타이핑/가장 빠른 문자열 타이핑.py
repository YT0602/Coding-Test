T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    x = len(A)
    y = len(B)
    cnt = A.count(B)
    typing = x - (cnt * y) + cnt
    print(f'#{tc} {typing}')