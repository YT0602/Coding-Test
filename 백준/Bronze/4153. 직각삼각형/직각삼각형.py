while True:
    numbers = list(map(int, input().split()))
    numbers.sort() #  오름차순 정렬
    if 0 in numbers: # 0포함이면 탈출
        break
    elif (numbers[0]**2) + (numbers[1]**2) == numbers[2]**2: # 피타고라스면 right
        print('right')
    else:
        print('wrong')
