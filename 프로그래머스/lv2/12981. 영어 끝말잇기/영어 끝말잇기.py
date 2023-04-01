def solution(n, words):
    answer = [words[0]]
    turn = 0
    num = 0
    for i in range(1, len(words)):
        if words[i] not in answer and words[i-1][-1] == words[i][0]:
            answer.append(words[i])
        else:
            turn = (i // n) + 1
            num = (i % n) + 1
            break
    print(answer)
    return [num, turn]