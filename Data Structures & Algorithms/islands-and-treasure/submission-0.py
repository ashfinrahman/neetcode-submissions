class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        levels = 0
        while q:
            levels += 1
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == INF:
                        q.append((ni, nj))
                        grid[ni][nj] = levels



        