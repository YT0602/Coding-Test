N = int(input())
s_dict = {}
for i in range(N):
    s = input()
    s_dict.setdefault(s, 0)
    s_dict[s] = len(s) # '단어' : 길이로 딕셔너리 만들기
s_dict = sorted(s_dict.items(), key = lambda x: (x[1], x)) # 길이, abc 순으로 정렬
for i in s_dict: # 하나씩 프린트
    print(i[0]) 
