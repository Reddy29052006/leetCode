from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = {}

        for row in grid:
            t = tuple(row)
            row_count[t] = row_count.get(t, 0) + 1

        ans = 0
        for col in zip(*grid):
            print(col)
            ans += row_count.get(col, 0)

        return ans


solution = Solution()
grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

print(solution.equalPairs(grid))
