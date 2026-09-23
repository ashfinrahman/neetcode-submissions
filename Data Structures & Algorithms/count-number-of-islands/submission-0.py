class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            visited.add((i, j))
            deque = collections.deque()
            deque.append((i, j))

            while deque:
                rowr, colc = deque.popleft()
                directions = [[1, 0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = rowr + dr, colc + dc
                    if (r in range(row) and
                        c in range(col) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        deque.append((r, c))
                        visited.add((r, c))

        for i in range(row):
            for j in range(col):
                if (grid[i][j] == "1" and (i, j) not in visited):
                    bfs(i,j)
                    islands += 1
        return islands

        