# In two linked lists find the node from which intersection happens
# Time complexity O(A+B), space complexity O(11)

from LinkedList import LinkedList,Node

def intersection(ll1,ll2):
    if ll1.tail is not ll2.tail:
        return False
    len1=len(ll1)
    len2=len(ll2)
    diff=abs(len1-len2)
    
    longer=ll1 if len1>len2 else ll2
    shorter=ll2 if len1>len2 else ll1

    lNode=longer.head
    sNode=shorter.head
    for i in range(diff):
        lNode=lNode.next
    while lNode is not sNode:
        lNode=lNode.next
        sNode=sNode.next
    return lNode


def addSameNode(ll1,ll2,value):
    tempNode=Node(value)
    ll1.tail.next=tempNode
    ll1.tail=tempNode

    ll2.tail.next=tempNode
    ll2.tail=tempNode

ll1=LinkedList()
ll2=LinkedList()

ll1.generate(3,0,10)
ll2.generate(3,0,10)

addSameNode(ll1,ll2,14)
addSameNode(ll1,ll2,3)

print(intersection(ll1,ll2))