N = int(input())
start = 1
x = 6
count = 0
while True:
    if N == 1:
        print(1)
        break
    elif start < N <= start + x:
        print(count + 2)
        break
    else:
        start = start + x
        x += 6
        count += 1

