def solution(brown, yellow):
    answer = []
    total = brown + yellow
    x = 0
    y = 0
    for i in range(2, int(total**0.5)+1):
        if total % i == 0:
            tmp_x = total // i
            tmp_y = i
            print(tmp_x, tmp_y)
            if total - (2*tmp_x + 2*(tmp_y-2)) == yellow:
                x = total // i
                y = i
                break
            
    return [x, y]