# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
     # Method to add an item to the queue
    def push(self, item): 
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
    
    # Method to remove an item from queue
    def pop(self):
        if self.head == None:
            return -1
        elif self.head == self.tail:
            temp = self.head.data
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends