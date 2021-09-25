
def reverseWord(st):
    sl = list(s)
    start = 0
    end = len(sl)-1
    while start<end:
        sl[start], sl[end] = sl[end], sl[start]
        start+=1
        end-=1
    listtostr = ''.join(str(i) for i in sl)
    return listtostr           
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends