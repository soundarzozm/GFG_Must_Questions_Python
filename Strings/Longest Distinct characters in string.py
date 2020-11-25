for _ in range(int(input())):
    
    dick = {}
    l_pt = 0
    r_pt = 1
    max1 = 0
    l_pt_old = 0
    
    string = input()

    dick[string[0]] = 0
    
    for i in range(1, len(string)):
        
        if string[i] not in dick.keys():
            r_pt = i
            dick[string[i]] = i
            max1 = max(r_pt - l_pt + 1, max1)

        else:
            r_pt = i
            l_pt = dick[string[i]] + 1
            
            for j in range(l_pt_old, l_pt):
                if string[j] in dick.keys():
                    dick.pop(string[j])
            
            l_pt_old = l_pt
                        
            dick[string[i]] = i
            max1 = max(r_pt - l_pt + 1, max1)

    print(max1) 