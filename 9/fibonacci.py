# fib_arr = []
def fibonacci(num):
    if num == 1 or num == 0:
        return 1
    else:
        # print("{},".format(fibonacci(num - 1) + fibonacci(num - 2)),end = "")
        # fib_arr.append(fibonacci(num - 1) + fibonacci(num - 2))
        return fibonacci(num - 1) + fibonacci(num - 2)
def calc_fib_arr(size):
    fib_arr = []
    for i in range(0,size):
        fib_arr.append(fibonacci(i))
    return fib_arr
if __name__ == "__main__":
    print("input Num:",end="")
    size = int(input())
    print(calc_fib_arr(size))
    # print(fib_arr)
