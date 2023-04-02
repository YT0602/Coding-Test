def solution(people, limit):
    ans = 0
    people.sort()
    
    a = 0
    b = len(people)-1
    print(people)
    
    while a <= b:
        # 현재 인원 중 가장 가벼운 사람과 가장 무거운 사람 합이 무게 초과하지 않는다면 같이 탑승   
        if people[a] + people[b] <= limit:
            a += 1
        # 아니면 무거운 사람만 탑승
        b -= 1
        ans += 1

    return ans