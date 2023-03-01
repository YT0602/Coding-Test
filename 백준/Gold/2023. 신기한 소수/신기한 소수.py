import sys
input = sys.stdin.readline

N = int(input())


def sosu(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def special(n):
    if len(str(n)) == N:
        print(n)
    for i in range(1, 10, 2):
        if sosu(n*10 + i):
            special(n*10+i)


special(2)
special(3)
special(5)
special(7)