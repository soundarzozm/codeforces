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
def solve(n, nums):
    if n < 2:
        return -1

    # Check if already beautiful
    for i in range(1, n):
        if (abs(nums[i-1] - nums[i]) <= 1):
            return 0

    if n == 2:
        if abs(nums[0] - nums[1]) <= 1:
            return 0
        return -1

    ascending = True
    descending = True
    for i in range(1, n):
        if (nums[i-1] > nums[i]):
            ascending = False

    for i in range(n-1, 0, -1):
        if (nums[i-1] < nums[i]):
            descending = False

    if ascending or descending:
        return -1

    return 1

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        nums = inlt()
        print(solve(n, nums))
