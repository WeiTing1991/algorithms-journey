"""
bubble sort 
Time complexity O(n*2)
Space complexity O(1)
"""



def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        swapped = False # check the ararry is sorted 
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1]= elements[j+1], elements[j]
                
                swapped = True
        if not swapped:
            break

def bubble_sort_by_key(elements, key=None):

    size = len(elements)
    
    for i in range(size-1):
        swapped = False # check the ararry is sorted 
        for j in range(size-1-i):
            # make key here !!!
            a = elements[j][key]
            b = elements[j+1][key]
            
            if a > b :
                elements[j], elements[j+1]= elements[j+1], elements[j]
                
                swapped = True
        if not swapped:
            break



if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
        
    print(elements)
    
    elements_list = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]
    
    
    bubble_sort_by_key(elements_list, key = 'transaction_amount')
        
    print(elements_list)
    
    
