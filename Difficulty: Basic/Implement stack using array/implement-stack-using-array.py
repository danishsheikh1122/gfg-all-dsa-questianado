#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
        self.top=-1
    
    #Function to push an integer into the stack.
    def push(self,data):
            self.arr.append(data)
            self.top+=1
            return data
    
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.top==-1:
            return -1
        else:
            popped_elem=self.arr.pop()
            self.top-=1
            return popped_elem
        
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()
        print("~")

# } Driver Code Ends