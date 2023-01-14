A = int(input())
B = int(input())
C = int(input())
x = str(A * B * C)
for i in range(10):
    count = 0
    for j in range(len(x)):
        if x[j] == str(i):
            count += 1
    print(count)