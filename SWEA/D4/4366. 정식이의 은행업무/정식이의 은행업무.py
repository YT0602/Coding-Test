def solve():
    for i in range(len(num2)):
        # 모든 자리수 한번씩 바꾸면서 비교
        num2[i] = (num2[i]+1) % 2
        # 2진수 -> 10진수
        num = 0
        for n in num2:
            num = num*2 + n
        # 10진수 -> 3진수
        conv3, t = [], num
        while t > 0:
            conv3.insert(0, t % 3)
            t //= 3

        # 바꾼 수를 뒤집어서 뒤에서부터 비교
        r1, r2, cnt = conv3[::-1], num3[::-1], 0
        # 인덱스 벗어나면 안되니까 둘 중 짧은거기준
        for j in range(min(len(r1), len(r2))):
            if r1[j] != r2[j]:
                cnt += 1
        cnt += abs(len(r1)-len(r2))
        # 딱 한개만 틀리다면 10진수 수 반환
        if cnt == 1:
            return num

        # 원상복구
        num2[i] = (num2[i] + 1) % 2


T = int(input())
for tc in range(1, T+1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))

    ans = solve()
    print(f'#{tc} {ans}')