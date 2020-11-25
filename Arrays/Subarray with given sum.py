for _ in range(int(input())):
    
    n, s = map(int, input().split())
    
    arr = list(map(int, input().split()))
    #print(n, s)
    #print(arr)
    flag = 0
    start = 0 
    end = 0 
    sum1 = 0
    
    while(end!=n+1):
        if sum1<s:
            sum1+=arr[end]
            end+=1
        elif sum1>s:
            sum1-=arr[start]
            start+=1
        elif sum1==s:
            flag=1
            break
        print("Start: ", start)
        print("End: ", end)
        print()
    
    if flag==0:
        print(-1)
    else:
        print(start+1, end)