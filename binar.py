def solution(num):

    count_zero, count_one, count_0 = 0, 0, 0

    a_list, list_count = [], []

    a = bin(num)

    for i in a:
        a_list.append(i)

    a_list = a_list[2:]

    for i in a_list:
        if i == '1':
            count_one += 1
        elif i == '0':
            count_zero += 1

    for i in a_list:
        if i == '1':
            list_count.append(count_0)
            count_0 = 0
            continue
        else:
            count_0 += 1

    if count_zero == 0 or count_one == 1:
        return 0, a_list
    else:
        return max(list_count), a_list


print(solution(1041))
