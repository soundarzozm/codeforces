import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))

############ ---- Code Here ---- ############


def solve(w, h, a, b, x1, y1, x2, y2):
    dx1 = x1 % a
    dy1 = y1 % b

    dx2 = x2 % a
    dy2 = y2 % b

    vertical = (dx1 == dx2) and ((x1 != x2) or (dy1 == dy2))
    horizontal = (dy1 == dy2) and (y1 != y2)

    if (vertical or horizontal):
        return "Yes"
    return "No"


if __name__ == "__main__":
    for _ in range(inp()):
        w, h, a, b = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())
        print(solve(w, h, a, b, x1, y1, x2, y2))
