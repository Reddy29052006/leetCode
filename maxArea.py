from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        for i in range(n):

            for j in range(i+1, n):
                b = min(height[i], height[j])
                l = j-i
                area = max(area, (l*b))

        return area


solution = Solution()

print(solution.maxArea([1, 1]))
