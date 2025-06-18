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


def solve(k, a, b, x, y):
    # (remaining_k_after_B - a) // x + 1

    ans_1 = 0
    k_1 = k

    if (k_1 >= a):
        ans_1 = (k_1 - a) // x + 1
        k_1 = k - ans_1 * x

    if (k_1 >= b):
        ans_1 += (k_1 - b) // y + 1

    ans_2 = 0
    k_2 = k

    if (k_2 >= b):
        ans_2 = (k_2 - b) // y + 1
        k_2 = k - ans_2 * y

    if (k_2 >= a):
        ans_2 += (k_2 - a) // x + 1

    return max(ans_1, ans_2)


if __name__ == "__main__":
    for _ in range(inp()):
        k, a, b, x, y = invr()
        print(solve(k, a, b, x, y))
