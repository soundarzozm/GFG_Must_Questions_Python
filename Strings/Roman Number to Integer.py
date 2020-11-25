for _ in range(int(input())):
    
    roman = input()
    
    dick = {"I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
    }
    
    integer = dick[roman[-1]]
    
    if len(roman) > 1:
        
        for i in range(len(roman) - 2, -1, -1):
            
            if dick[roman[i]] >= dick[roman[i+1]]:
                integer += dick[roman[i]]
            else:
                integer -= dick[roman[i]]
                
    print(integer) 