sing = list(map(int, input().split()))
a = [1,2,3,4,5,6,7,8]
d = list(reversed(a))
if sing == a:
    print('ascending')
elif sing == d:
    print('descending')
else:
    print('mixed')