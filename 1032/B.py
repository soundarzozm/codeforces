import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
     
############ ---- Code Here ---- ############
def solve(n, s):
    mySet = set()
    mySet.add(s[0])
    mySet.add(s[n-1])

    for i in range(1, n-1):
        if s[i] in mySet:    
            return "Yes"
        mySet.add(s[i])
    return "No"

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        s = insr()
        print(solve(n, s))
