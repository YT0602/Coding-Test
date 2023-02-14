N, M = map(int, input().split())
note = dict()
for i in range(N):
    password = list(input().split())
    note[password[0]] = password[1]
for i in range(M):
    print(note[input()])