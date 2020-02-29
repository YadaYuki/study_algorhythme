from time_deco import timeit 
import random
@timeit("insert_sort",ndigits=10)
def insert_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while True:
            if j == -1:
                break
            if temp < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = temp
    return arr
if __name__ == "__main__":
    # print()
    insert_sort([90,40,5,100,200])
    insert_sort([random.random() for i in range(1,100)])
    # print()