# your task is to complete this function
# function should return an integer
def atoi(string):
    try:
        result = int(string)
    except:
        result = -1
    return result    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends