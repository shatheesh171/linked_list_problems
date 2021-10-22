# Sum two linked list with numbers in reverse order and represent the sum in linked list in reverse order,
#  each element has one digit

#Time and space both are O(n) here

from LinkedList import LinkedList,Node

def sumList(ll1,ll2):
    n1=ll1.head
    n2=ll2.head
    ll=LinkedList()
    carry=0
    
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.add(result%10)
        carry=int(result/10)
    return ll



ll1=LinkedList()
ll2=LinkedList()
ll1.generate(3,1,9)
ll2.generate(3,1,9)
print(ll1)
print(ll2)
print(sumList(ll1,ll2))
