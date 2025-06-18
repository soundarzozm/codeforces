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
def solve(n, s, nums):
    minValue = nums[0]
    maxValue = nums[n-1]

    if s < minValue:
        return maxValue - s
    if s > maxValue:
        return s - minValue

    if (maxValue - s) > (s - minValue):
        ans = (s - minValue) * 2
        ans += maxValue - s
        return ans
    
    ans = (maxValue - s) * 2
    ans += s - minValue
    return ans

def binarySearch(nums, n, t):
    left = 0
    right = n - 1
    ans = left

    while (left <= right):
        mid = (left + right) // 2

        if nums[mid] > t:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid

    return ans

if __name__ == "__main__":
    for _ in range(inp()):
        n, s = invr()
        nums = inlt()
        print(solve(n, s, nums))
