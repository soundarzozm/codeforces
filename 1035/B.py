import sys
input = sys.stdin.readline
import math

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
def solve(n, px, py, qx, qy, a):
    dist = math.dist([px, py], [qx, qy])
    a.append(dist)
    a.sort()

    if sum(a[:-1]) < a[-1]:
        return "No"

    return "Yes"

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        px, py, qx, qy = invr()
        a = inlt()
        print(solve(n, px, py, qx, qy, a))
