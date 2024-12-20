#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count=0
        temp=n
        while n>0:
            lastdigit=n%10
            if lastdigit!=0 and temp%lastdigit==0:
                count+=1
            n=n//10
        return count
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends