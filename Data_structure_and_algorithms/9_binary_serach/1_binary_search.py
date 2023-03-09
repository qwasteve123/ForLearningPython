from util import time_it

@time_it
def linear_serach(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_serach(numbers_list,number_to_find):
    
    left_index = 0
    right_index = len(numbers_list)
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        if mid_number < number_to_find:
            left_index = mid_index +1
        else:
            right_index = mid_index -1
    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index)//2
    mid_number = numbers_list[mid_index]

    if mid_index >=len(numbers_list) or mid_index < 0:
        return -1

    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index +1
    else:
        right_index = mid_index -1

    return binary_search_recursive(numbers_list,number_to_find,left_index,right_index)





if __name__ == '__main__':
    numbers_list = [12,15,17,19,21,24,45,67,80]
    number_to_find = 90

    # numbers_list = [i for i in range(100000001)]
    # number_to_find = 100000000


    index = linear_serach(numbers_list,number_to_find)
    index = binary_search_recursive(numbers_list,number_to_find,0,len(numbers_list))
    print(index)