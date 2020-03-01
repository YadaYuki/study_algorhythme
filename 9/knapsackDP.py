class Item():
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

class KnapSack():
    def __init__(self):
        # self.max_time = time
        self.item_arr = [Item("",-1,-1) for i in range(5)]
        self.num_to_str = lambda num: chr(64 + num) 
        self.name_arr = [self.num_to_str(i) for i in range(1,6)]
        self.weight_arr = [i for i in range(1,6)]
        self.price_arr = [100,300,350,500,650]
        self.item_arr = [Item(self.name_arr[i],self.price_arr[i],self.weight_arr[i]) for i in range(5)]
    # set Item Info

    # def show_knap(self,item):
    #     for i in range():

if __name__ == "__main__":
    ks = KnapSack()
    MAX_WEIGHT = 6
    ITEM_NUM = len(ks.item_arr)
    value_arr = [[-1]* (MAX_WEIGHT + 1)] * ITEM_NUM
    value_arr[0] = [0,100,100,100,100,100,100]
    # calculate best value
    for i in range(1,ITEM_NUM):
        for j in range(MAX_WEIGHT + 1):
            if j >= ks.item_arr[i].weight:
                left_weight = j - ks.item_arr[i].weight
                value = ks.item_arr[i].price + value_arr[i-1][left_weight]
                if value >= value_arr[i-1][j]:
                    value_arr[i][j] = value
                else:
                    value_arr[i][j] = value_arr[i-1][j]
            elif i == j == 0:
                value_arr[i][j] = 0
            else:
                value_arr[i][j] = value_arr[i-1][j]
    print(value_arr)

