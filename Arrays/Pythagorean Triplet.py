#User function Template for python3
class Solution:

	def checkTriplet(self, arr, n):
    	dic = {}

    	arr.sort

    	for i in range(n):
    	    arr[i] = arr[i]**2
    	    dic[arr[i]] = 1

    	for i in range(n-1):
    	    for j in range(i, n):
    	        if arr[i]+arr[j] in dic.keys():
    	            return True
    	return False        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes\n")
        else:
            print("No\n")
        tc -= 1

# } Driver Code Ends