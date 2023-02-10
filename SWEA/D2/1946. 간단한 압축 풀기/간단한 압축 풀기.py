T = int(input())
for tc in range(1, T+1):
    N = int(input())
    text = []  # 문자, 횟수
    original = ''
    for i in range(N):
        x, num = input().split()
        original = original + x*int(num)

    print(f'#{tc}')
    for k in range(1, len(original) + 1):
        if k % 10:
            print(original[k - 1], end='')
        else:
            print(original[k - 1], end='\n')
    print()