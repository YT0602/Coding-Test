import sys
input = sys.stdin.readline


def girl_switch(list, num, S, E):
    if S < 1 or E > N or list[S] != list[E]:
        return S + 1, E - 1
    elif list[S] == list[E]:
        return girl_switch(list, num, S-1, E+1)


N = int(input())
switch = [0] + list(map(int, input().split()))
p = int(input())
for i in range(p):
    s, num = map(int, input().split())
    if s == 1:
        for j in range(1, N+1):
            if j % num == 0:
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
    else:
        if num == N or num == 1:
            if switch[num] == 1:
                switch[num] = 0
            else:
                switch[num] = 1
        else:
            s_switch = girl_switch(switch, num, num-1, num+1)[0]
            e_switch = girl_switch(switch, num, num-1, num+1)[1]
            for j in range(s_switch, e_switch+1):
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1


for i in range(1, N+1):
    if i % 20 != 0:
        print(switch[i], end=' ')
    else:
        print(switch[i], end='\n')