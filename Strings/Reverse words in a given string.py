for _ in range(int(input())):
    
    arr = input().split(".")
    
    string = ""
    
    for i in range(len(arr) - 1, 0, -1):
        string += arr[i] + "."
    
    string += arr[0]
    
    print(string)