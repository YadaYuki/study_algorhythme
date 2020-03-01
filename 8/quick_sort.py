import random
class QuickSort():
    def __init__(self,size):
        self.size = size
        # initialize random number array 0 ~ 19
        self.array = [random.randint(0,20) for i in range(self.size)]
    
    def sort_array(self,start,end):
        # if the element is not 1
        if start < end:
            pivod = self.divide_array(start,end)
            # left side of pivod
            self.sort_array(start,pivod-1)
            # right side of pivod
            self.sort_array(pivod+1,end)

        # pass
    def divide_array(self,head,tail):
        # initialize right and left index
        left = head + 1
        right = tail
        while True:
            # search value bigger than base
            while left < tail and self.array[left] < self.array[head]:
                left += 1
            while self.array[right] > self.array[head]:
                right -= 1

            if right <= left:
                break
            temp = self.array[left]
            self.array[left] = self.array[right]
            self.array[right] = temp

            right -= 1
            left += 1

        temp = self.array[head] 
        self.array[head] = self.array[right] 
        self.array[right] = temp 

        return right
         


if __name__ == "__main__":
    print("input array size:",end = "")
    size = int(input())
    qs = QuickSort(size)
    print("Before sorting:{array}".format(array = qs.array))
    qs.sort_array(0,qs.size - 1)
    print("After sorting:{array}".format(array = qs.array))