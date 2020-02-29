class HashTable():
    def __init__(self,size):
        self.size = size
        self.array = [-1] * size
    
    def insert_value(self,value):
        pos = value % self.size
        # not same
        if self.array[pos] != -1:
            self.array[pos] = value

    def search_value(self,value):
        pos = value % self.size
        if self.array[pos] == value:
            return pos
        else:
            return -1

if __name__ == "__main__":
    ht = HashTable(10)
    ht.insert_value(134)
    print(ht.search_value(134))
