for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    result_string = ""
    
    for i in range(n//2):
        result_string += str(arr[n-i-1]) + " "
        result_string += str(arr[i]) + " "
            
    if (n%2 != 0):
        result_string += str(arr[n//2]) 
        
    print(result_string)   