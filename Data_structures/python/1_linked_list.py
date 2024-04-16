# linked list
# singly, Doubly, Circular
# resource : https://www.geeksforgeeks.org/linked-list-set-1-introduction/?ref=lbp


"""

Big O of the linked list
Accessing Time of an element : O(n)
Search time of element O(n)
Insertion O(1) --> push, insert_after 
Deletion O(1)

"""

# Node class
class Node:

    # initialize the object
    def __init__(self, data=None):
        self.data = data # assign data
        self.next = None # Initialize next as null
        self.prev = None
    
# singly linked list     
class LinkedList:
    
    
    # initalize the Linked
    def __init__(self):
        self.head = None
    
    # This function prints contents of linked list
    def print_list(self):
        
        if self.head == None:
            print("linked list is empty")
            return 
        
        temp = self.head
        while temp: 
            print(f"{temp.data}")
            temp = temp.next
    
    # insert the new node at the begining of the linked list
    def push(self, new_data):
        # Allocate the Node & Put the new data as head
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node
    
    # Get the length of the linked list
    def get_length(self):
        temp = self.head # initialise the temp
        count = 0
        
        while (temp):
            count += 1
            temp = temp.next
        return count
    
    # Inserts a new node after the given prev_node
    def insert_after(self, prev_node, new_data):
        # check if the given prev_node exists
        if prev_node is None:
            print("The given previos node must in Linkedlist")
            return
        # create new node & put in the data
        new_node = Node(new_data)
        # make next of new Node as next prev_node
        new_node.next = prev_node.next
        # 
        prev_node.next = new_node
    
    # Inserts a new node at the end of linked list
    def append(self, new_data):
        # create new node & put in the data
        new_node = Node(new_data)
        # if the linked list is emppty, then make tthe new node as head
        if self.head is None:
            self.head = new_node
            return 
        
        # else traverse till the last node 
        last = self.head
        while last.next:
            last = last.next
        # change the next of last node 
        last.next = new_node

    # remove the node at the given index/key
    def delete_node(self, key):
        
        temp = self.head
        
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # search for the key to be deleted, keep track of the prvious node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        # if key was not present in linked list
        if temp == None:
            return
        
        # Unlick the node from linked list
        prev.next = temp.next
        temp = None

        
# doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
        # check if the node is none
        if self.head is None:
            print("the linked list is empty")
        return 

        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data) + '-->'
            temp = temp.next
        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)   
    


if __name__ == '__main__':
    # initalize the class llist
    llist = LinkedList()
    
    ## linking the list
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    # llist.head.next = second
    # second.next = third

    llist.append([0, 5, 6,])
    llist.push(5)
    llist.insert_after(llist.head.next, [0, 5, 10, 1])
    llist.push(100)
    llist.print_list()
    
    print("\n")
    llist.delete_node(100)
    llist.print_list()
    print("Count of nodes is :", llist.get_length())
