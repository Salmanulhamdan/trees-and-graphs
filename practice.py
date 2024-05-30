class Node:
    def __init__(self,data,next=None) -> None:
        self.data=data
        self.next=next





# class Linkedlist:
#     def __init__(self) -> None:
#         self.head=None

    
l1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    
#linked list one

item1=Node(1)
item2=Node(2)
item3=Node(3)
item4=Node(4)
item5=Node(7)
item6=Node(8)


# Linking nodes
item1.next = item2
item2.next = item3
item3.next = item4
item4.next = item5
item5.next = item6

# linkedlist2

data1=Node(6)
data2=Node(8)
data3=Node(9)
data4=Node(10)
data5=Node(11)


data1.next=data2
data2.next=data3
data3.next=data4
data4.next=data5

# Function to print the linked list
def print_linked_list(node):
    current = node
    while current:
        print(current.data, end=" -> ")
        current = current.next
        
    print("None")

# Print the linked list starting from item1
print_linked_list(item1)
print_linked_list(data1)
print_linked_list(l1)










        