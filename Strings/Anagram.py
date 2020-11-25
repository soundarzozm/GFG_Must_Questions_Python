for _ in range(int(input())):
    
    string1, string2 = input().split()
    
    dick = {}
    
    flag = "NO"
    
    if len(string1) == len(string2):
        
        for i in range(len(string1)):
            if string1[i] in dick.keys():
                dick[string1[i]] += 1
            else:
                dick[string1[i]] = 1
                
            if string2[i] in dick.keys():
                dick[string2[i]] -= 1
            else:
                dick[string2[i]] = -1
        
        flag = "YES"        
        for i in dick.keys():
            if dick[i] > 0:
                flag = "NO"
                break
            
    print(flag)
    