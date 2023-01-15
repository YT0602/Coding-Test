numbers = list(map(int, input().split()))
result = 0
for i in range(len(numbers)):
    a = numbers[i]**2
    result += a
print(result%10)