import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if s[x][y] < s[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
dp = [[-1] * n for i in range(m)]

print(dfs(m - 1, n - 1))



##########################################

# 2차원 메모이제이션 dp + dfs

def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        x1, y1 = x + graph[x][y], y
        x2, y2 = x, y + graph[x][y]

        if 0 <= x1 < n and 0 <= y1 < n: dp[x][y] += dfs(x1, y1)
        if 0 <= x2 < n and 0 <= y2 < n: dp[x][y] += dfs(x2, y2)

    return dp[x][y]


n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
dp = [[-1] * n for i in range(n)]

print(dfs(0, 0))