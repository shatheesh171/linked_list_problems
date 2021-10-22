# Write a program to remove duplicate elements from unsorted linked list

from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        node=ll.head
        visited=set([node.value])
        while node.next:
            if node.next.value in visited:
                node.next=node.next.next
            else:
                visited.add(node.next.value)
                node=node.next
        return ll

ll=LinkedList()
ll.generate(10,0,15)
ll.add(15)
ll.add(15)
print(ll)
removeDups(ll)
print(ll)