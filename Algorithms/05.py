"""
Merge Sort is a Divide and Conquer algorithm.

"""


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(list_a, list_b):
    sorted_list = []

    len_a = len(list_a)
    len_b = len(list_b)

    i = j = 0
    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            sorted_list.append(list_a[i])
            i+=1
        else:
            sorted_list.append(list_b[j])
            j+=1
    
    while i < len_a:
        sorted_list.append(list_a[i])
        i+=1
    
    while j < len_a:
        sorted_list.append(list_b[j])
        j+=1
    
    return sorted_list
    


if __name__ == "__main__":

    arr = [10,3,15,7,8,23,98,29]

    print(merge_sort(arr))