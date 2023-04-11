def solution(record):
    ans = []
    # 단어 분류
    for i in record:
        ans.append(list(i.split(' ')))

    # 이름 설정
    name = dict()
    for i in ans:
        name.setdefault(i[1], 0)
        if len(i) == 3:
            name[i[1]] = i[2]

    # 기록 입력
    result = []
    for i in range(len(record)):
        if ans[i][0] == 'Enter':
            result.append(f'{name[ans[i][1]]}님이 들어왔습니다.')
        elif ans[i][0] == 'Leave':
            result.append(f'{name[ans[i][1]]}님이 나갔습니다.')

    return result