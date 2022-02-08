# binary tree 
# binary search Tree

# every node has at most 2 child tree


# type BFS and DFS
# In order traversal
# Pre order traveral
# Post order traveral

import timeit

class BinarySearchTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return 
        if data < self.data:
            # add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)            

    def in_order_traversal(self):
        elements = []
        
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
            
        
        # visit base node
        elements.append(self.data)
        
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()        
        
        return elements
    
    def post_order_traversal(self):
        elements = [] 
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()   

        elements.append(self.data)    
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data] 
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()   
  
        return elements
    
    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            """
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
            """
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_node(max_val)
        
        return self
        
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # search left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            # search right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    print(f"{elements}" + "\n")
    
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root 

if __name__ == '__main__':
    
    number_list = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(number_list)
    print("in_order_traversal: ", number_tree.in_order_traversal()) 
    print("pre_order_traversal: ", number_tree.pre_order_traversal()) 
    print("post_order_traversal: ", number_tree.post_order_traversal())    
    
    
    print("\n")
    
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.sum())
    print("Is data in the list ", number_tree.search(20))
    print("Is data in the list ", number_tree.search(50))
    
    
    print("in_order_traversal: ", number_tree.in_order_traversal()) 
    print(number_tree.delete_node(20))
    print("in_order_traversal: ", number_tree.in_order_traversal()) 
    
    startime = timeit.default_timer()
    print(f"Execution time is: {timeit.default_timer() - startime}")