def binary_search(num_arr,num):
    pos = -1
    left = 0
    right = len(num_arr)-1
    while True:
        middle = int((left + right) / 2)
        if num > middle:
            left = middle
        elif num < middle:
            right  = middle
        elif num == middle:
            # found
            pos = middle
            break
        if right - left == 1:
            # num does not exist in the array
            break
        print("right:",right)
        print("left:",left)
    return pos
            


if __name__ == "__main__":
    num_arr = list(range(100))
    print("num_arr:",num_arr)
    num = input()
    print(num ,"is in ",binary_search(num_arr,int(num)))


