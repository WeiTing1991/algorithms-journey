# General Tree

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self # new  node as a parent
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent   

        return level
    
    def print_tree(self, property_name):
        
        if property_name == 'both':
            v = self.name + "("+ self.designation +")"
        elif property_name == 'name':
            v = self.name
        else:
            v = self.designation
            
        spaces = ' ' * self.get_level() * 5 
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + v)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def print_tree_level(self, property_name, level):
        
        if self.get_level() > level: # if return -- break the funtion
            return
        
        if property_name == 'both':
            v = self.name + "("+ self.designation +")"
        elif property_name == 'name':
            v = self.name
        else:
            v = self.designation
            
        spaces = ' ' * self.get_level() * 5 
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + v)
        if self.children:
            for child in self.children:
                child.print_tree_level(property_name, level)
    


def build_product_tree():
    
    laptop = TreeNode("laptop", "workstaion")
    laptop.add_child(TreeNode("Mac", "Builded_2020"))
    laptop.add_child(TreeNode("Dell", "Precsion_7730"))
    
    
    
    mobile = TreeNode("mobile", "mobile")
    mobile.add_child(TreeNode("iphone", "12_plus"))
    mobile.add_child(TreeNode("ipad", "pro_2018"))
    mobile.add_child(TreeNode("iphone", "6S"))
    
    
    
    device = TreeNode("Electronics", "2022")
    device.add_child(laptop)
    device.add_child(mobile)
    
    return device
    #print(root.children[0].children[0].data)
    #print(root.children[0].children[1].data)
    
if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree("both")
    root_node.print_tree_level("both", 1)