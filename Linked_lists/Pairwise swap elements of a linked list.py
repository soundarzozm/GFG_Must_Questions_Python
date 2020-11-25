
"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping

def pairWiseSwap(head):
    
    def swap(head):

        ptr_1 = head
        ptr_2 = head.next

        if (ptr_2 == None):
            return ptr_1, None

        ptr_3 = ptr_2.next

        ptr_2.next = ptr_1
        ptr_1.next = ptr_3

        return ptr_2, ptr_2.next

    ptr_last = head
    ptr_first = head
    ptr_second = head.next
    ptr_next = head
    
    if (ptr_second == None):
        return head
    
    i = 1
    
    while(ptr_first):
        
        if i == 1:
            head_final, ptr_last = swap(ptr_first)
            ptr_first = ptr_first.next
            i += 1

        else:
            ptr_last.next, ptr_last = swap(ptr_first) 
            ptr_first = ptr_first.next
        
    return head_final    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = pairWiseSwap(lis.head)
        printList(head)

# } Driver Code Ends