for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = arr[n-1]
    arr2 = []
    
    for i in range(n-1, -1, -1):
        if arr[i] >= max1:
            arr2.append(arr[i])
            max1 = arr[i]
    
    arr2.reverse()
    
    for i in range(len(arr2)-1):
        print(arr2[i], end = " ")
    
    print(arr2[-1], end = "\n")    