def solution(N):

    count_zero, count_one = 0, 0

    list_num, list_count_zero = [], []

    a = bin(N)

    for number in a:
        list_num.append(number)

    list_num = list_num[2:]

    for num in list_num:
        if num == '1':
            count_one += 1
            list_count_zero.append(count_zero)
            count_zero = 0
        else:
            count_zero += 1

    if max(list_count_zero) == 0 or count_one == 1:
        return 0, list_num
    else:
        return max(list_count_zero), list_num


print(solution(1041))
