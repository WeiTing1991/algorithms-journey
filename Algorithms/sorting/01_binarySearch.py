# Binary Search
"""

This is practice for binarysearch
key: split the array as left and rihgt
The data should be sorted.



O(n)
Log(n)

"""

from util import time_it


@time_it
def linear_search(num_list, num_to_find):
    for index, element in enumerate(num_list):
        if element == num_to_find:
            return index
    return -1


@time_it
def binary_search(num_list, num_to_find):
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = num_list[mid_index]

        if mid_number == num_to_find:
            return mid_index
        if (
            mid_number < num_to_find
        ):  # this means number is in right hand side of the list
            left_index = mid_index + 1
        else:  # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1


def binary_search_recursive(num_list, num_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(num_list) or mid_index < 0:
        return -1

    mid_number = num_list[mid_index]

    if mid_number == num_to_find:
        return mid_index
    if mid_number < num_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(num_list, num_to_find, left_index, right_index)


def find_all_occurances(num_list, num_to_find):
    index = binary_search(num_list, num_to_find)
    indices = [index]
    # find indices on left hand side
    ind = index - 1
    while ind >= 0:
        if num_list[ind] == num_to_find:
            indices.append(ind)
        else:
            break
        ind -= 1

    ind = index + 1
    # find indices on right hand side
    while ind <= len(num_list):
        if num_list[ind] == num_to_find:
            indices.append(ind)
        else:
            break
        ind += 1

    return sorted(indices)


if __name__ == "__main__":
    # numbers = [1,4,6,9,10,5,7]
    # numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    # number_to_find = 15

    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]

    # numbers_list.sort()
    number_to_find = 15

    # big array
    # numbers_list = [i for i in range(100000000)]
    # number_to_find = 15000000

    index_l = linear_search(numbers_list, number_to_find)
    print(index_l, "\n")

    index_b = binary_search(numbers_list, number_to_find)
    print(index_b)

    index_b_r = binary_search_recursive(
        numbers_list, number_to_find, 0, len(numbers_list)
    )
    print(index_b_r, "\n")

    indeices = find_all_occurances(numbers_list, number_to_find)
    print(indeices, "\n")
