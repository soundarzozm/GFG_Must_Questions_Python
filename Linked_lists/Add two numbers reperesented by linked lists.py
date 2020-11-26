def reverseList(head):
    
        prev = None
        current = head

        while(current is not None):
        
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        
        head = prev

        return head
        
    first = reverseList(first)
    second = reverseList(second)
    
    result = LinkedList()
    
    carry = 0
    
    while (first==None and second==None):
        
        bruh = first.data + second.data + carry
        
        first = first.next
        second = second.next
        
        if bruh > 9:
            carry = 1
            bruh = bruh//10
        
        else:
            carry = 0
            
        result.insert(bruh)
        
    return reverseList(result).head