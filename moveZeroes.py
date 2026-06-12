from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0
        n = len(nums)
        while r < n:

            if nums[r] != 0:
                if r != l:
                    nums[l] = nums[r]
                    nums[r] = 0
                l += 1

            r += 1

        return None


solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)
