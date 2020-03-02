import random
import copy
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
        self.knap_arr = [{"gene":[random.randint(0,1) for i in range(len(self.item_arr))],"suitable_rate":0} for j in range(self.children_num)]
    
    def calc_suitable_rate(self):
        for i in self.knap_arr:
            suitable_rate = 0
            weight = 0
            for j in range(len(i["gene"])):
                suitable_rate += self.item_arr[j].price * i["gene"][j]
                weight += self.item_arr[j].weight * i["gene"][j]

            if weight <= MAX_WEIGHT:
                i["suitable_rate"] = suitable_rate
            else:
                i["suitable_rate"] = 0
    def sort_knap_arr_by_suitable_rate(self):
        # sort by insert sort
        for i in range(1,len(self.knap_arr)):
            j = i - 1
            temp = self.knap_arr[i]
            while True:
                if j == -1:
                    break
                if temp["suitable_rate"] > self.knap_arr[j]["suitable_rate"]:
                    self.knap_arr[j + 1] = self.knap_arr[j]
                else:
                    break
                j -= 1
            self.knap_arr[j + 1] = temp
    def print_knap_arr(self):
        print("{:>20}".format(str(self.name_arr)))
        for knap in self.knap_arr:
            print("{:>20}:{:>3}".format(str(knap["gene"]),knap["suitable_rate"]))
    
    def delete_half_knap(self):
        print("DELETE UNDER 50%")
        top_half_knap = self.knap_arr[0:int(len(self.knap_arr)/2 + 0.5)]
        # knap_arr is 2nd zigen → deep copy is needed.
        self.knap_arr[int(len(self.knap_arr)/2 + 0.5):] = copy.deepcopy(top_half_knap)
        self.print_knap_arr()
        
    def sudden_change(self):
        # sudden change on under half 50%
        under_half_idx = int(self.children_num/2 + 0.5)
        for i in range(under_half_idx,self.children_num):
            for j in range(len(self.knap_arr[i]["gene"])):
                # sudden change parameterized by self.sudden_change_rate
                if random.random() >= (1-self.sudden_change_rate):
                    print("Sudden Changed in i:{i} j:{j}".format(i=i,j=j))
                    self.knap_arr[i]["gene"][j] = 1 - self.knap_arr[i]["gene"][j]
    
    def cross_child(self):
        under_half_idx = int(self.children_num/2 + 0.5)
        for i in range(under_half_idx,self.children_num - 1):
            cross_over_point = random.randint(0,len(self.item_arr))
            for j in range(cross_over_point,len(self.item_arr)):
                temp = self.knap_arr[i]["gene"][j]
                self.knap_arr[i]["gene"][j] = self.knap_arr[i + 1]["gene"][j] 
                self.knap_arr[i + 1]["gene"][j] = temp
    
    def calc_optimal_rate(self):
        # first generation
        self.calc_suitable_rate()
        self.sort_knap_arr_by_suitable_rate()
        self.print_knap_arr()
        self.delete_half_knap()

        for generation in range(2,self.generation+1):
            self.sudden_change()
            self.cross_child()
            self.calc_suitable_rate()
            self.sort_knap_arr_by_suitable_rate()
            print("generation:{generation}".format(generation=generation))
            self.print_knap_arr()
            self.delete_half_knap()

        print("optimal match:{} value:{}".format(str(self.knap_arr[0]["gene"]),self.knap_arr[0]["suitable_rate"]))


if __name__ == "__main__":
    print("sudden_change_rate:",end="")
    sudden_change_rate = float(input())
    print("generation:",end="")
    generation = int(input())
    print("children_num:",end="")
    children_num = int(input())
    kga = knapsackGA(sudden_change_rate,generation,children_num)
    kga.calc_optimal_rate()
                
                
