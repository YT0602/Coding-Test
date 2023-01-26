import sys

N = int(sys.stdin.readline())
st = []
for _ in range(N):
    name= sys.stdin.readline().split()
    if name[0] == 'push':
        st.append(int(name[1]))
    if name[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    if name[0] == 'size':
        print(len(st))
    if name[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    if name[0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
