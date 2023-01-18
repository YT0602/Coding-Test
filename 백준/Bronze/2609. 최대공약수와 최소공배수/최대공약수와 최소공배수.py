N, M = map(int, input().split())

def gcd(x, y):
    while y > 0:
        if x % y == 0:
            return y
        x, y = y, x % y
        
def lcm(x, y):
    return x * y // (gcd(x, y))

print(gcd(N, M))
print(lcm(N, M))