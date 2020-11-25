for _ in range(int(input())):
    
    string = input()
    
    flag = -1
    for i in range(len(string) - 1, -1, -1):
        if string[i] == "1":
            flag = i
            break
            
    print(flag)