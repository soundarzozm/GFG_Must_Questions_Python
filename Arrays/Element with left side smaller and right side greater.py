for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    flag = -1
    
    left_dic = {}
    right_dic = {}
    
    buf = arr[0]
    for i in range(n):
        if buf < arr[i]:
            buf = arr[i]
        left_dic[i] = buf
        
    buf = arr[n-1]
    for i in range(n-1, -1, -1):
        if buf > arr[i]:
            buf = arr[i]
        right_dic[i] = buf
        
    for i in range(1, n-1):
        if arr[i]>=left_dic[i-1] and arr[i]<=right_dic[i+1]:
            flag = arr[i]
            break
    print(flag)    