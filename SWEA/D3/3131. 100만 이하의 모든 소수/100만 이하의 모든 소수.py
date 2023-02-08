def isPrime(n):
    result = [2]
    for i in range(3, n, 2):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


print(*isPrime(1000000))