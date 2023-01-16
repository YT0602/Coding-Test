N = int(input())
count = 0
for i in range(N, 0, -1):
    k = list(map(int, str(i)))
    result = sum(k) + i
    if result == N:
        count = i

print(count)
