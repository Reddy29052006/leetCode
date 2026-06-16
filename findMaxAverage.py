from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        WindowSum = sum(nums[:k])
        MaxSum = WindowSum

        for i in range(k, len(nums)):
            WindowSum += nums[i]-nums[i - k]
            MaxSum = max(MaxSum, WindowSum)

        return MaxSum / k


solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4

print(solution.findMaxAverage(nums, k))
