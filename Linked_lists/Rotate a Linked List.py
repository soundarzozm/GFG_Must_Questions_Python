# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# This function should rotate list counter-
# clockwise by k and return head node
def rotateList(head, k):
    
    i = 1
    ptr = head
    while(i!=k):
        ptr = ptr.next
        i+=1
    
    if (ptr.next == None):
        return head
    
    new_head = ptr.next
    ptr.next = None
    
    ptr = new_head
    
    while(ptr.next!=None):
        ptr=ptr.next
    
    ptr.next = head
    
    return new_head



#{ 
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = rotateList(lis.head,k)
        printList(head)
# } Driver Code Ends