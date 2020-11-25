for _ in range(int(input())):

    string = input()
    start = 0
    maxLength = 1
    length = len(string) 

    low = 0
    high = 0

    for i in range(1, length):

        #EVEN
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1

        #ODD
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
            
    print(string[start : start+maxLength])