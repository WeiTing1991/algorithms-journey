
"""
Basic comprehension of list
python list is a daymanic array


Let size of array be n
Aceesing Time O(1)
Search Time O(n)
Insertion Time O(n)
Deletion Time O(n)


"""

max = int(input("enter max number:"))

odd_number = []

for i in range(1, max):
    if i%2 == 1:
        odd_number.append(i)
print("odd number:", odd_number)



lst = [i for i in range(5)]

while lst: # if list is not empty
    print(lst.pop(-1))