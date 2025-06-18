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
def solve(n, m, mat):
    maxValue = 0

    for i in range(n):
        for j in range(m):
            maxValue = max(maxValue, mat[i][j])

    rows = [0] * n
    cols = [0] * m
    total = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == maxValue:
                rows[i] += 1
                cols[j] += 1
                total += 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == maxValue:
                if rows[i] + cols[j] - 1 == total:
                    return maxValue - 1
            else:
                if rows[i] + cols[j] == total:
                    return maxValue - 1

    return maxValue

if __name__ == "__main__":
    t = inp()
    for _ in range(t):
        n, m = invr()

        mat = []
        for r in range(n):
            mat.append(inlt())

        print(solve(n,m,mat))
