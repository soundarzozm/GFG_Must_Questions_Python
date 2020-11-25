for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = 0
       
    left_max = 0
    right_max = 0
       
    lo = 0
    hi = n-1
       
    while(lo <= hi):  
      
        if(arr[lo] < arr[hi]): 
          
            if(arr[lo] > left_max): 
                left_max = arr[lo] 
                
            else:   
                result += left_max - arr[lo] 
                
            lo+= 1
          
        else: 
          
            if(arr[hi] > right_max): 
                right_max = arr[hi] 
                
            else: 
                result += right_max - arr[hi] 
                
            hi-= 1
    
    print(result)