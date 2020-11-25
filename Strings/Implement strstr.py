#FOR BETTER TIME COMPLEXITY USE Z-ALGORITHM TO SKIP RELEVANT CHARACTERS IF MISMATCH
#O(M+N)

'''
	Your task is to return the index of the pattern
	present in the given string.
	
	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.
	
'''
def strstr(s,p):
    index = -1

    for i in range(len(s) - len(p) + 1):
        if s[i] == p[0]:
            for j in range(len(p)):
                if s[i+j] == p[j]:
                    if j == len(p)-1:
                        index = i
                        return(index)
                else:
                    break
    return(index)  

#{ 
#  Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends