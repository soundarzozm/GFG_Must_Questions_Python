#Without Hashing
for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        try:
            if arr[i]!=i+1:
                print(i+1)
                break
        except:
            print(n)

#With Hashing
"""for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    
    for i in range(n-1):
        dic[arr[i]] = 1
    
    for j in range(1, n+1):
        if j not in dic.keys():
            print(j)
            break
"""          