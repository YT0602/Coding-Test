from collections import deque

def solution(priorities, location):
    ans = 0
    priorities = deque(priorities)
    while True:
        # 맨 앞이 중요도 가장 크면 pop하고 순서 +1, 타겟 인덱스 -1
        if priorities[0] == max(priorities):
            priorities.popleft()
            ans += 1
            location -= 1
        # 아니면
        else:
            # 앞에서 빼고 뒤에 추가하고 인덱스 -1
            priorities.append(priorities.popleft())
            # 이때 인덱스가 -1이 되면 마지막 인덱스로 바꿔줌
            location -= 1
            if location == -1:
                location = len(priorities) - 1
        # 타겟 인덱스가 -1이면 pop이 됐으므로 종료
        if location == -1:
            break
    return ans