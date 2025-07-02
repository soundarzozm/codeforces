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
def solve(n, k, s):
    ones = 0

    for char in s:
        if char == "1":
            ones += 1

    if ones <= k or n < (2 * k):
        return "Alice"

    return "Bob"

if __name__ == "__main__":
    for _ in range(inp()):
        n, k = invr()
        s = insr()
        print(solve(n, k, s))
