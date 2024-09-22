"""
quick sort
Lomuto Partition Scheme(start form end)
Hoare Partition Scheme(start form first)

average time complexity O(nlogn)
worst case time complexity O(n*2)

"""
#Lomuto Partition Scheme(start form end)
def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    
    pivot_index = start 
    pivot = elements[end] # first pivot
    
    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, pivot_index, elements)
            pivot_index +=1       
             
    swap(pivot_index, end, elements) # swap pivot and end
    return pivot_index


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pr_index = partition(elements, start, end)
        quick_sort(elements, start, pr_index-1) # Left partition
        quick_sort(elements, pr_index+1, end) # right partition





if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)