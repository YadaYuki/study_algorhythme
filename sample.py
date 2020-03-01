from time_deco import timeit

@timeit("print_hundred",10)
def print_hundred():
    for i in range(1,100):
        print(i)

@timeit("print_num",10)
def print_num(num):
    for i in range(1,num):
        print(i)

@timeit("print_num2",10)
def print_num2(num1,num2):
    for i in range(num1,num2):
        print(i)


if __name__ == "__main__":
    # no arguement
    print_hundred()
    # one arguement
    print_num(10)
    # two argument
    print_num2(10,100)