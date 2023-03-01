import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
cnt = 0

for i in range(N):
    s = 0
    e = N - 1
    while s < e:
        if numbers[i] == numbers[s]+numbers[e]:
            if s != i and e != i:
                cnt += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif numbers[i] < numbers[s]+numbers[e]:
            e -= 1

        elif numbers[i] > numbers[s]+numbers[e]:
            s += 1

print(cnt)