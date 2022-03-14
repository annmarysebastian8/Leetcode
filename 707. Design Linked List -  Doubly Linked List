
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        
        while index != 0:    # Increasing curr pointer until we reach the index
            curr = curr.next
            index -= 1
        return curr.val
    
    
    def addAtHead(self, val: int) -> None:
        
        newNode = Node(val)
        newNode.next = self.head
        
        if self.head:
            self.head.prev = newNode
        
        self.head = newNode
        
        self.size += 1
        
        if self.size == 1:
            self.tail = newNode
        
    def addAtTail(self, val: int) -> None:
        
        newNode = Node(val)
        newNode.prev = self.tail
        
        if self.tail:
            self.tail.next = newNode
        
        self.tail = newNode
        
        self.size += 1
        
        if self.size == 1:
            self.head = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        newNode = Node(val)
        
        if index < 0 or index > self.size:
            return -1
        
        elif index == 0:
            self.addAtHead(val)
        
        elif index == self.size:
            self.addAtTail(val)
        
        else:
            curr = self.head
            
            while index-1 != 0:
                curr = curr.next
                index -= 1
                
            newNode = Node(val)
            
            newNode.next = curr.next
            curr.next.prev = newNode
            
            curr.next = newNode
            newNode.prev = curr
            
            self.size += 1
            
            
    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return -1
        
        elif index == 0:
            
            if self.head.next:
                self.head.next.prev = None
                
            self.head = self.head.next
            
            self.size -= 1
            
            if self.size == 0:
                self.tail = None
        
        elif index == self.size-1:
            
            if self.tail.prev:
                self.tail.prev.next = None
            
            self.tail = self.tail.prev
            
            self.size -= 1
            
            if self.size == 0:
                self.head = None
        
        else:
                
            cur = self.head
            while index-1 != 0:

                cur = cur.next
                index -= 1

            cur.next = cur.next.next
            cur.next.prev = cur
            
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
