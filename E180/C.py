import sys
input = sys.stdin.readline
import bisect

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
def solve(n, a):
    ans = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            # Find the first index where a[i] + a[j] <= a[k]
            target = a[i] + a[j]
            it = bisect.bisect_left(a, target, j + 1)
            end = it - (j + 1)
            if end == 0:
                continue

            # Now find ak such that ak > a[n-1] - a[i] - a[j]
            target2 = a[n - 1] - a[i] - a[j]
            it2 = bisect.bisect_right(a, target2, j + 1, j + end + 1)
            ans += (j + end + 1) - it2

    return ans


if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        nums = inlt()
        print(solve(n, nums))
