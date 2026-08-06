class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, idx, visited):
            if idx == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[idx]:
                return False

            if (r, c) in visited:
                return False

            visited.add((r, c))

            found = (
                dfs(r + 1, c, idx + 1, visited) or
                dfs(r - 1, c, idx + 1, visited) or
                dfs(r, c + 1, idx + 1, visited) or
                dfs(r, c - 1, idx + 1, visited)
            )

            visited.remove((r, c))
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True

        return False
