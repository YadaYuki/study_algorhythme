from time_deco import timeit 

@timeit("factorial",ndigits = 10)
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    num = int(input())
    print(factorial(num))