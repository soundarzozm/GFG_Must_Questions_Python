#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
def sortedMerge(head_A, head_B):
    
    ptr_a = head_A
    ptr_b = head_B
    
    if head_A.data > head_B.data:
        ptr_final = head_B
        ptr_b = head_B.next
    elif head_A.data <= head_B.data:
        ptr_final = head_A
        ptr_a = head_A.next
    
    ptr = ptr_final
    #print(ptr.data)
    
    i = 1
    while (ptr_a != None and ptr_b != None):
        
        if ptr_a.data > ptr_b.data:

            ptr.next = ptr_b
            ptr_b = ptr_b.next
            ptr = ptr.next
            #print(ptr.next.data)
            
            
        elif ptr_a.data <= ptr_b.data:

            ptr.next = ptr_a
            ptr_a = ptr_a.next
            ptr = ptr.next
            #print(ptr.next.data)
    
        i += 1

    if ptr_a == None:
        
        ptr.next = ptr_b
        
        while(ptr_b):
            #print(ptr_b.data)
            ptr_b = ptr_b.next
            
            
    else:
        
        ptr.next = ptr_a
        
        while(ptr_a):
            #print(ptr_a.data)
            ptr_a = ptr_a.next
        
          
    return ptr_final       

#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends