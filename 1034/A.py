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
def solve(n):
    if (n % 4 == 0):
        return "Bob"
    return "Alice"

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        print(solve(n))
