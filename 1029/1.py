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
def solve(n, x, doors):
    left = 0
    right = n - 1

    while (left < right):
        if (doors[left] == 0):
            left += 1
        elif (doors[right] == 0):
            right -= 1
        else:
            break

    if (right - left + 1) > x:
        return "NO"
    return "YES"

if __name__ == "__main__":
    for _ in range(inp()):
        n, x = invr()
        doors = inlt()
        print(solve(n, x, doors))
