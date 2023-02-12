import sys
input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split()))
plus = 1
p_cnt = 1
minus = 1
m_cnt = 1
for i in range(N-1):
    if num[i] > num[i+1]:
        m_cnt += 1
        if plus < p_cnt:
            plus = p_cnt
        p_cnt = 1
    elif num[i] < num[i+1]:
        p_cnt += 1
        if minus < m_cnt:
            minus = m_cnt
        m_cnt = 1
    else:
        p_cnt += 1
        m_cnt += 1
if plus < p_cnt:
    plus = p_cnt
if minus < m_cnt:
    minus = m_cnt

if plus < minus:
    print(minus)
else:
    print(plus)