def inorder(n):
    if n > N:
        return
    elif n <= N:
        inorder(2*n)
        print(nodes[n-1][1], end='')
        inorder(2*n+1)


for tc in range(1, 11):
    N = int(input())
    nodes = [list(input().split()) for _ in range(N)]
    print(f'#{tc}', end=' ')
    inorder(1)

    print()