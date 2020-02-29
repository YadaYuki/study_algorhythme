class LinkedList():
    def __init__(self,next,value):
        self.next = next
        self.value = value

    def set_value(self,next,value):
        self.next = next
        self.value = value

def insert_item(prev,next,value,arr,p):
    arr[p].set_value(next,value)
    arr[prev].next = p
    
def delete_item(prev,next,arr):
    arr[prev].next = next

def print_linked_list(linked_list,top):
    i = top
    while True:
        item = linked_list[i]
        print("value({next}):{value}".format(value = item.value,next = item.next))
        i = item.next
        if item.next == -1:
            break


if __name__ == "__main__":
    univ_arr = [LinkedList(1,"あなた") for i in range(10)]
    # list[0].next = 3
    # list[0].value="青学"
    univ_arr[0].set_value(3,"青学")
    # list[1].next = -1
    # list[1].value = "早稲田"
    univ_arr[1].set_value(-1,"早稲田")
    # list[2].next = 1
    # list[2].value = "慶応"
    univ_arr[2].set_value(1,"慶応")
    # list[3].next = 2
    # list[3].value = "明治"
    univ_arr[3].set_value(2,"明治")
    # list[4].next = 0
    # list[4].value = "立教"
    univ_arr[4].set_value(0,"立教")
    print_linked_list(univ_arr,top=4)
    print("insert item 中央 between 青学 and 立教")
    insert_item(prev = 4,next = 0 ,value = "中央",arr=univ_arr,p = 5)
    print_linked_list(univ_arr,top=4)
    print("delete 慶応")
    delete_item(prev = 3,next = 1,arr = univ_arr)
    print_linked_list(univ_arr,top=4)


