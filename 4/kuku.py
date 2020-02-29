from time_deco import timeit 

@timeit("kuku",10)
def print_kuku():
    for i in range(1,10):
        for j in range(1,10):
            print("{:^4}".format(i*j),end="")
        print()

if __name__ == "__main__":
    print_kuku()

