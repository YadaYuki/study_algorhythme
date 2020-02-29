def euclid_method(a,b):
    while True:
        if a==b:
            break
        elif a > b:
            a = a - b
        elif a < b:
            b = b - a
    return a

def get_min_mul(a,b):
    max_div = euclid_method(a,b)
    mul =a * b / max_div 
    return mul

if __name__ == "__main__":
    a,b = input().split(" ")
    print(get_min_mul(int(a),int(b)))