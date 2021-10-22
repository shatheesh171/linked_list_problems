#Partition a linked list around a value of x, less than x come before and greater than come after

from LinkedList import LinkedList
 
def partition(ll,x):
    node=ll.head
    ll.tail=node

    while node:
        nextNode=node.next
        node.next=None
        if node.value<x:
            node.next=ll.head
            ll.head=node
        else:
            ll.tail.next=node
            ll.tail=node
        node=nextNode
    if ll.tail.next:
        ll.tail.next=None

ll=LinkedList()
ll.generate(10,0,99)
print(ll)
partition(ll,15)
print(ll)