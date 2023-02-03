cnt = 0


def recursion(s, l, r):
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        global cnt
        cnt += 1
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    global cnt
    cnt = 0
    cnt += 1
    return recursion(s, 0, len(s) - 1)


N = int(input())
for i in range(N):
    pa = list(input())
    print(isPalindrome(pa), cnt)