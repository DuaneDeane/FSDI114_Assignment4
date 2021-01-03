class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("Where is the node? Node can't be null!")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node
    
    def append(self, new_data):

        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    
    def printList(self, node):

        print("In a forward direction, traveled")
        while(node is not None):
            print(" % d" %(node.data))
            last = node
            node = node.next

        print("In a reverse direction, traveled")
        while(last is not None):
            print(" % d" %(last.data))
            last = last.prev

if __name__=='__main__':

    llist = DLL()
    llist.append(9)
    llist.push(3)
    llist.push(6)
    llist.append(1)
    llist.insertAfter(llist.head.next, 4)

    print('DLL is: ')
    llist.printList(llist.head)