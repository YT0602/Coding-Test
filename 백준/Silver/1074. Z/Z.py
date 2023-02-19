import sys
input = sys.stdin.readline

N, r, c = map(int,  input().split())
cnt = 0


def Z(num, row, col):
    global cnt
    if num == 2:
        for i in range(row, row+num):
            for j in range(col, col + num):
                cnt += 1
                if i > r and j > c:
                    return
                elif i == r and j == c:
                    print(cnt-1)
                    return
        return
    else:
        if r < row + num//2 and c < col + num//2:
            Z(num//2, row, col)
        elif r < row + num//2 and col + num//2 <= c:
            cnt += (num // 2 * num // 2)
            Z(num//2, row, col+num//2)
        elif row + num // 2 <= r and c < col + num // 2:
            cnt += (num // 2 * num // 2) * 2
            Z(num//2, row+num//2, col)
        else:
            cnt += (num//2 * num//2) * 3
            Z(num//2, row+num//2, col+num//2)


Z(2**N, 0, 0)
