import random
class Item():
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
MAX_WEIGHT = 6

class knapsackGA():
    
    def __init__(self,sudden_change_rate,generation,children_num):
        self.item_arr = [Item("",-1,-1) for i in range(5)]
        self.num_to_str = lambda num: chr(64 + num) 
        self.name_arr = [self.num_to_str(i) for i in range(1,6)]
        self.weight_arr = [i for i in range(1,6)]
        self.price_arr = [100,300,350,500,650]
        self.item_arr = [Item(self.name_arr[i],self.price_arr[i],self.weight_arr[i]) for i in range(5)]
        self.sudden_change_rate = sudden_change_rate
        self.generation = generation
        self.children_num =  children_num
        self.item_is_include_arr = [{"item_is_include":[random.randint(0,1) for i in range(len(self.item_arr))],"suitable_rate":0} for j in range(self.children_num)]
    
    def calc_suitable_rate(self):
        for i in self.item_is_include_arr:
            suitable_rate = 0
            weight = 0
            for j in range(len(i["item_is_include"])):
                suitable_rate += self.item_arr[j].price * i["item_is_include"][j]
                weight += self.item_arr[j].weight * i["item_is_include"][j]
                
            if weight <= MAX_WEIGHT:
                i["suitable_rate"] = suitable_rate
            else:
                i["suitable_rate"] = 0

if __name__ == "__main__":
    kga = knapsackGA(0.1,3,8)
    print(kga.item_is_include_arr)
    kga.calc_suitable_rate()
    print(kga.item_is_include_arr)
                
                
