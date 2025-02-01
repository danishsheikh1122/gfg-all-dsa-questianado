#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        # just use left shift with 1 1<<i&(n)
        
        temp=n&(1<<k)
        # 100
        # 001
        # 010
        # 100
        # 100
        # &
        # 100
        # 100
        # is set the return 1 else 0
        return True if temp!=0 else False

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("true")
        else:
            print("false")
        print("~")    
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends