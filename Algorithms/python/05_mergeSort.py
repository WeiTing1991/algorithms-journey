"""
Merge Sort is a Divide and Conquer algorithm.

"""

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(list_a, list_b, arr):
    
    len_a = len(list_a)
    len_b = len(list_b)

    i = j = k = 0 # k is index to arr
    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            arr[k] = list_a[i]
            i+=1
        else:
            arr[k] = list_b[j]
            j+=1
        k+=1

    # Add the last one which miss in first while condition 
    while i < len_a:
        arr[k] = list_a[i]
        i+=1
        k+=1
    
    while j < len_b:
        arr[k] = list_b[j]
        j+=1
        k+=1    

#
def merge_sort_by_key(elements, key, descending=False):

    if len(elements) <= 1:
        return elements

    left_list = merge_sort_by_key(elements[0:len(elements)//2], key, descending=False)
    right_list = merge_sort_by_key(elements[len(elements)//2:], key, descending=False)
    sorted_list = merge(left_list, right_list, key, descending=False)

    return sorted_list


def merge(left_list, right_list, key, descending=False):

    merged = []
    if descending:
        while len(left_list)>0 and len(right_list)>0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))
    else:
        while len(left_list)>0 and len(right_list)>0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))
    
    merged.extend(left_list)
    merged.extend(right_list)    

    return merged


if __name__ == "__main__":

    arr = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    # for lst in arr:
    #     merge_sort(lst)
    # print(arr)
    # print('\n')

    elements = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        ]

    sorted_elements = merge_sort_by_key(elements, key='time_hours', descending=True)
    print(sorted_elements)
