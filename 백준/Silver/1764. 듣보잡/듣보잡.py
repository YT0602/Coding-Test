import sys
input = sys.stdin.readline

N, M = map(int, input().split())
st = set()
ans = []
for i in range(N):
    st.add(input().strip())
for j in range(M):
    text = input().strip()
    if text in st:
        ans.append(text)

ans.sort()
print(len(ans))
for k in ans:
    print(k)