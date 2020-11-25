for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    
    for i in range(n):
        if arr[i] == 0:
            cnt0+=1
        elif arr[i]==1:
            cnt1+=1
        else:
            cnt2+=1
    
    for i in range(0, cnt0):
        arr[i] = 0
    
    for i in range(cnt0, cnt1 + cnt0):
        arr[i] = 1
        
    for i in range(cnt0 + cnt1, cnt2 + cnt1 + cnt0):
        arr[i] = 2
        
    for i in range(n-1):
        print(arr[i], end=" ")
    
    print(arr[n-1], end="\n")    
        