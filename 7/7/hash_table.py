class HashTable():
    def __init__(self,size):
        self.size = size
        self.array = [-1] * size
    
    def insert_value(self,value):
        init_pos = value % self.size
        pos = init_pos
        # not already has num
        while True:
            if self.array[pos] == -1:
                self.array[pos] = value
                break
            # move to next address 
            pos += 1
            # if pos over length of array , pos back to 0
            pos = pos % self.size
            # array is already full.
            if pos == init_pos:
                break

    def search_value(self,value):
        init_pos = value % self.size
        pos = init_pos
        while True:
            if self.array[pos] == value:
                return pos
            pos += 1
            pos = pos % self.size
            # value does not exist in array
            if pos == init_pos:
                break


if __name__ == "__main__":
    ht = HashTable(10)
    # store number
    while True:
        print("Insert:",end="")
        num = int(input())
        if num < 0:
            break
        ht.insert_value(num)
        print("inserted!")
    # search number
    while True:
        print("Search:",end="")
        num = int(input())
        if num < 0:
            break
        print("{num} is in {p}".format(num=num,p=ht.search_value(num)))
    print(ht.array)

