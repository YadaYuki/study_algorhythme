from time_deco import timeit 
class Fibonacci():
    def __init__(self,size):
        self.size = size
        self.array = [-1 for i in range(size)]

    @timeit("calc_fibonacci",ndigits=10)
    def calc_fibonacci(self,num):
        if self.array[num] == -1 :
            print("calculating {}".format(num))
            if num == 0 or num == 1:
                self.array[num] = 1
                return 1
            else:
                self.array[num] = self.calc_fibonacci(num - 1) + self.calc_fibonacci(num - 2)
                # return self.calc_fibnacci(num - 1) + self.calc_fibnacci(num - 2)
        return self.array[num]

if __name__ == "__main__":
    fib = Fibonacci(100)
    fib.calc_fibonacci(99)
    print(fib.array)