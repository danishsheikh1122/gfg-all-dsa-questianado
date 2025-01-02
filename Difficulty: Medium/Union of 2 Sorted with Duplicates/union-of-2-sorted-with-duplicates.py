#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
            # code here 
        s = []  # List to store the merged unique values
        seen = set()  # Set to track seen elements
        i, j = 0, 0
    
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if a[i] not in seen:
                    s.append(a[i])
                    seen.add(a[i])
                i += 1
            elif b[j] < a[i]:
                if b[j] not in seen:
                    s.append(b[j])
                    seen.add(b[j])
                j += 1
            else:  # a[i] == b[j], add only one
                if a[i] not in seen:
                    s.append(a[i])
                    seen.add(a[i])
                i += 1
                j += 1
    
        # Add remaining elements from a
        while i < len(a):
            if a[i] not in seen:
                s.append(a[i])
                seen.add(a[i])
            i += 1
    
        # Add remaining elements from b
        while j < len(b):
            if b[j] not in seen:
                s.append(b[j])
                seen.add(b[j])
            j += 1
    
        return s
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends