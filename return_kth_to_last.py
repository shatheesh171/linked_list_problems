#Find nth to last element of singly linked list
from LinkedList import LinkedList, Node

def nthToLast(ll,n):
    ptr1=ll.head
    ptr2=ll.head

    for i in range(n):
        if ptr2 is None:
            return
        ptr2=ptr2.next

    while ptr2:
        ptr1=ptr1.next
        ptr2=ptr2.next
    return ptr1


ll=LinkedList()
ll.generate(10,0,99)
print(nthToLast(ll,3))
print(ll)