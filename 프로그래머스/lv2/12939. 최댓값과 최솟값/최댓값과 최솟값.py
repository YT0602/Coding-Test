def solution(s):
    answer = ''
    number = list(map(int, s.split(' ')))
    number.sort()
    answer += str(number[0]) + ' ' + str(number[-1])
    return answer
