def euclid_method(a,b):
    while True:
        if a == b:
            break
        elif a > b:
            a = a - b
        elif a < b:
            b = b - a
    return a

if __name__ == "__main__":
    a,b = input().split(" ")
    print(euclid_method(int(a),int(b)))