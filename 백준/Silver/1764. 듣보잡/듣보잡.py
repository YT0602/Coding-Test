N, M = map(int, input().split())
st = set()
ans = []
for i in range(N):
    st.add(input())
for j in range(M):
    text = input()
    if text in st:
        ans.append(text)
print(len(ans))
ans.sort()
for k in ans:
    print(k)