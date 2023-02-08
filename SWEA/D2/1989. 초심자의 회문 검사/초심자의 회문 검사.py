T = int(input())
for tc in range(1, T+1):
    word = list(input())
    answer = 0
    if word == word[::-1]:
        answer = 1
    print(f'#{tc} {answer}')