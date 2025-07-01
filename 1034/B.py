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
def solve(n, j, k, nums):
    player = nums[j-1]

    if k == 1:
        if max(nums) != player:
            return "No"

    return "Yes"


if __name__ == "__main__":
    for _ in range(inp()):
        n, j, k = invr()
        nums = inlt()
        print(solve(n, j, k, nums))
