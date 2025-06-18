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
    year = 0
    for i in range(4):
        year = year * 10 + int(n[i])

    root = findSquareRoot(year)
    if root == -1:
        return -1

    return f"0 {root}"

def findSquareRoot(n):
    if n == 0 or n == 1:
        return n
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    for _ in range(inp()):
        n = insr()
        print(solve(n))
