class BstItem():
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

class Bst():
    ROOT_IDX = 0
    def __init__(self):
        self.bst = []
        self.item_idx = 0
        
    def add_bst_item(self,num):
        item = BstItem(value = num,left = -1 ,right = -1)
        self.bst.append(item)
        # the item is not root
        if self.item_idx != Bst.ROOT_IDX:
            # search from ROOT_INDEX
            current_idx = Bst.ROOT_IDX
            pos_is_not_find = True
            while pos_is_not_find:
                if num > self.bst[current_idx].value:
                    right_val = self.bst[current_idx].right
                    if right_val == -1:
                        # rightを配列の最後尾のidxの値にする
                        self.bst[current_idx].right = len(self.bst) - 1
                        pos_is_not_find = False
                        break
                    current_idx = right_val
                elif num < self.bst[current_idx].value:
                    left_val = self.bst[current_idx].left
                    if left_val == -1:
                        # leftを配列の最後尾のidxの値にする
                        self.bst[current_idx].left = len(self.bst) - 1
                        pos_is_not_find = False
                        break
                    current_idx = left_val
        self.item_idx += 1
    
    def print_arr(self):
        for item in self.bst:
            print("value:{},right:{},left:{}".format(item.value,item.right,item.left))
    
    def search_value(self,num,current_idx = 0):
        # Not Found
        if current_idx == -1:
            return -1
        elif num == self.bst[current_idx].value:
            return current_idx
        elif num > self.bst[current_idx].value:
            return self.search_value(num,self.bst[current_idx].right)
        elif num < self.bst[current_idx].value:
            return self.search_value(num,self.bst[current_idx].left)

if __name__ == "__main__":
    bst = Bst()
    bst.add_bst_item(10)
    bst.add_bst_item(11)
    bst.add_bst_item(12)
    bst.add_bst_item(8)
    bst.add_bst_item(7)
    bst.add_bst_item(9)
    bst.print_arr()
    print(bst.search_value(10))