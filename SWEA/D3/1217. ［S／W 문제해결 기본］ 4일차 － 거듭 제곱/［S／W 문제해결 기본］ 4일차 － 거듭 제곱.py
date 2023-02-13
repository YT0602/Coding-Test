for tc in range(1, 11):
    T = int(input())
    num, x = map(int, input().split())
    ans = num**x
    print(f'#{T} {ans}')