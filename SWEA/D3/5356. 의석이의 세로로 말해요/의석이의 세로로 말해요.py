T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    mx_len = 0
    # 가장 긴 문자열 길이 구하기
    for i in arr:
        mx_len = max(mx_len, len(i))
    # 가장 긴 문자열 길이에 맞춰서 공백 삽입
    for i in arr:
        while len(i) < mx_len:
            i.append(' ')
    # 배열을 열별로 묶기
    arr_col = list(map(list, zip(*arr)))
    # 공백 제거해서 조인 후 출력
    print(f'#{tc}', end=' ')
    for i in arr_col:
        print(''.join(i).replace(' ', ''), end='')
    print()