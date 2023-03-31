def solution(n):
    answer = 0
    number = list(map(int, str(n)))
    for i in number:
        answer += i
    return answer