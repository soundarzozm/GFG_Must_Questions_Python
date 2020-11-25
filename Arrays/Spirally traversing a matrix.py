for _ in range(int(input())):
    
    m, n = map(int, input().split())
    arr1 = list(map(int, input().split()))
    
    a = []
    
    for i in range(0, m*n, n):
        a.append(arr1[i:i+n])
    
    k = 0
    l = 0
    result = ""
 
    while (k < m and l < n):
 
        for i in range(l, n):
            result += str(a[k][i]) + " "
        k += 1
 
        for i in range(k, m):
            result += str(a[i][n-1]) + " "
        n -= 1
 
        if (k < m):
            for i in range(n-1, l-1, -1):
                result += str(a[m-1][i]) + " "
            m -= 1
 
        if (l < n):
            for i in range(m-1, k-1, -1):
                result += str(a[i][l]) + " "
            l += 1
            
    print(result)