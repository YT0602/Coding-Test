def solution(phone):
    ans = True
    phone.sort()

    for i in range(len(phone)-1):
        l = len(phone[i])

        for j in range(l):
            if phone[i+1][j] != phone[i][j]:
                break
        else:
            ans = False


    return ans