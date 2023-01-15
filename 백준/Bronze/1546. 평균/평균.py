N = int(input())
score = list(map(int, input().split()))
M = max(score)
new = []
for i in range(len(score)):
    new.append(score[i] / M * 100)
print(sum(new)/len(new))