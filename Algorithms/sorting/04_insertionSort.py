"""
https://en.wikipedia.org/wiki/Insertion_sort

insertion sort

worst n*2
average n*2

better use in small array

"""

from array import array
from itertools import count


def insertion_sort(elements):

    median_num = elements[0]    
    for i in range(1, len(elements)): # consider first item is sorted.
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j] # swap 
            j = j - 1
        elements[j+1] = anchor

# insertion_sort
def place_to_insert(array, key):
    index = 0
    for item in array:
        if item > key:
            break
        else:
            index+=1
    return index
        
def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index] + [key] + array[index:]



if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]

    insertion_sort(elements)
    print(f'sorted array:{elements}')

    elements_2 = [2, 1, 5, 7, 2, 0, 5]

    stream = [] 
    count = 0
    while True:
        i = int(input())
        count += 1
        stream = insert_to_sorted(stream, i)
        if count%2 == 1:
            print(f"Mdian of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")








