for _ in range(int(input())):
    
    num_strings = int(input())
    
    strings = list(input().split())
    
    common_prefix = ""
    
    smol_string = min(strings)
    
    for i in range(len(smol_string)):
        
        for j in range(num_strings):
            
            if smol_string[i] == strings[j][i]:
                
                if j == num_strings-1:
                    common_prefix += strings[0][i]
                
            else:
                break
        
        if len(common_prefix) < 1:
            common_prefix = "-1"
            break
            
    print(common_prefix)  