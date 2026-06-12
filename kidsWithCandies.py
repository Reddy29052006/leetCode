from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCondies = max(candies)
        boolenValues = []
        for i in candies:
            boolenValues.append((i+extraCandies) >= maxCondies)

        return boolenValues


solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
