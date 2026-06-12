from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum = 0
        ans = []
        for i, curVal in enumerate(nums):
            ans.append(abs(totalSum - leftSum - curVal))
            leftSum += curVal
            totalSum -= curVal
        return ans


s = Solution()
print(s.leftRightDifference([10, 4, 8, 3]))
