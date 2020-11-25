for _ in range(int(input())):
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = []
    
    for i in range(0, n, k):
        x = arr[i:i+k]
        x.reverse()
        arr2 += x
        
    for i in range(n-1):
        print(arr2[i], end= " ")
        
    print(arr2[n-1], end="\n")  