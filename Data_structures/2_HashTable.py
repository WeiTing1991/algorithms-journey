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
            h += ord(char) # asking the length of char
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
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del ", index)
                del self.arr[arr_index][index]        


if __name__ == '__main__':
    
    arr_test = [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
    
    weather_dict = {'Jan 1': 27,
                    'Jan 2': 31,
                    'Jan 3': 23,
                    'Jan 4': 34,
                    'Jan 5': 37,
                    'Jan 6': 38,
                    'Jan 7': 29,
                    'Jan 8': 30,
                    'Jan 9': 35,
                    'Jan 10': 30}
    
    print(weather_dict['Jan 9'])
    
    
    """
    t = HashTable()
    t['march 6'] = 130
    
    t['march 17'] = 200
    print(t.arr)
    
    del t['march 6']
    print(t.arr)
    """