for _ in range(int(input())):
    
    str1 = input()
    str2 = input()
    
    str2acw = str2[2:] + str2[:2]
    str2cw = str2[-2:] + str2[:-2]
    
    if str2cw == str1 or str2acw == str1:
        print("1")
    else:
        print("0")