# Hash Table(Hash Map)
# complexity of search using dictionary is O(1)
# python use dictionary


## open file 
'''
with open(file, 'r') as f:
    

'''


def get_hash_01(key):
    h = 0 
    for char in key:
        h += ord(char) # asking the number of char
    return h % 100

r = get_hash_01("march 28")
print(r)



class HashTable:
    def __init__(self):
        self.MAX = 100 
        self.arr = [[]for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0 
        for char in key:
            h += ord(char) # asking the number of char
        return h % 100
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 & element[0]==key:
                self.arr[h][idx] = (key, val)
                found = True
                break
            
        if not found:
            self.arr[h].append((key, val))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None    


if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 130
    
    t['march 17'] = 200
    print(t.arr)