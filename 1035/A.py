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
def solve(a, b, x, y):
    diff = b - a
    cost = 0

    if diff == 0:
        return cost

    if a % 2 != 0 and diff == -1:
        return y

    if diff < 0:
        return -1

    if x <= y:
        return diff * x

    while diff > 0:
        if (a % 2 == 0):
            cost += y
        else:
            cost += x

        a += 1
        diff -= 1

    return cost

if __name__ == "__main__":
    for _ in range(inp()):
        a, b, x, y = invr()
        print(solve(a, b, x, y))
