class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    curr = linkedList
    while curr is not None:
        temp = curr.next
        while temp is not None and temp.value == curr.value:
            temp = temp.next
        curr.next = temp
        curr = temp
    return linkedList
