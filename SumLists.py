# Sum two linked list with numbers in reverse order and represent the sum in linked list in reverse order,
#  each element has one digit

from LinkedList import LinkedList,Node

def sumList(ll1,ll2):
    n1=ll1.head
    n2=ll2.head
    ll=LinkedList()
    ten=0
    
    while n1 or n2:
        sum=n1.value+n2.value+ten
        #print(sum)
        one=sum%10
        ten=int(sum/10)
        node=Node(one)
        n1=n1.next
        n2=n2.next
        if ll.head is None: 
            ll.head=node
            ll.tail=node
            continue
        ll.tail.next=node
        ll.tail=node
        #print("count")
        
    return ll



ll1=LinkedList()
ll2=LinkedList()
ll1.generate(3,1,9)
ll2.generate(3,1,9)
print(ll1)
print(ll2)
print(sumList(ll1,ll2))
