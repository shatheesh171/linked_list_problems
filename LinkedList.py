from random import randint

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self) -> str:
        return str(self.value)
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def __str__(self) -> str:
        values=[str(node.value) for node in self]
        return '->'.join(values)

    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result


    def add(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        return self.tail

    def generate(self,n,min_val,max_val):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_val,max_val))
        return self

# ll=LinkedList()
# ll.generate(10,0,99)
# print(ll)
# print(len(ll))