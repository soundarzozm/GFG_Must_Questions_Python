n = int(input())  
arr = list(map(int, input().split()))

cnt = 0
arrdic = {}

for i in range(n):
	arrdic[arr[i]]=1

#print(arrdic)

for l in range(n):

    for m in range(l+1, n):

        if arr[l]+arr[m] in arrdic.keys():
            cnt+=1
print(cnt)            


              


