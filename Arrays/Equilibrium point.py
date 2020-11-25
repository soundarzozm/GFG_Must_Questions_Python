n = int(input())
arr = list(map(int, input().split()))
    
flag = -1
i = 1
    
if n == 1:
    flag = 1

elif n==2:
    pass
        
else:
    cur = arr[1]
    left = arr[0]
    right = sum(arr[2:n])
        
    while(i < n-1):
        
        if left == right:
            flag = i+1
            break
        
        left += cur
        cur = arr[i+1]
        right-=cur
        i+=1
        
print(flag)