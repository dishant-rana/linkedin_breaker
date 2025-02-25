my_list = [1, 2, 3, 4, 5, 6]


def check_even(num_list):
    even_list = []
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(check_even(my_list))
