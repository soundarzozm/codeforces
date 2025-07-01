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
    ans = [0] * n
    ans[0] = 1
    ans[n-1] = 1

    minV = nums[0]
    maxV = nums[n-1]

    for i in range(1, n-1):
        if nums[i] < minV:
            ans[i] = 1
            minV = nums[i]

    for i in range(n-2, 0, -1):
        if nums[i] > maxV:
            ans[i] = 1
            maxV = nums[i]

    return "".join(str(x) for x in ans)

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        nums = inlt()
        print(solve(n, nums))
