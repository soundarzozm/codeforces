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
def solve(a, x, y):
    left = min(x, y)
    right = max(x, y)

    if (a < left or a > right):
        return "YES"
    return "NO"

if __name__ == "__main__":
    for _ in range(inp()):
        a, x, y = invr()
        print(solve(a, x, y))
