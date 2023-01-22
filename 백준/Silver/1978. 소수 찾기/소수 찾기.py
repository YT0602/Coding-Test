N = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if i == 1:
        pass
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
print(count)