"""
quick sort
Lomuto Partition Scheme(start form end)
Hoare Partition Scheme(start form first)

average time complexity O(nlogn)
worst case time complexity O(n*2)

"""
import sys


# Hoare Partition Scheme(start form first)
def swap(a, b, arr):
    if a!=b:
        #arr[a], arr[b] = arr[b], arr[a] #pythonic
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    
    pivot_index = start
    pivot = elements[pivot_index]
    
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1 
            
        while elements[end] > pivot:
            end-=1 
        
        if start < end:
            swap(start, end, elements)
            
    swap(pivot_index, end, elements)
    
    return end
    
        
def quick_sort(elements, start, end):
    if start < end:
        pr_index = partition(elements, start, end)
        quick_sort(elements, start, pr_index-1) # Left partition
        quick_sort(elements, pr_index+1, end) # right partition



if __name__ == '__main__':
    print(sys.getrecursionlimit())
    
    elements = [11, 9, 29, 7, 2, 15, 28]
    
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
    
    
    elements_arr = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]   
    
    for elements in elements_arr:
        quick_sort(elements, 0, len(elements)-1)
        print(f"sorted array: {elements}")
