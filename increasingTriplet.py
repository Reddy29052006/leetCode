from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


s = Solution()

print(s.increasingTriplet([6, 7, 1, 2]))      # False
print(s.increasingTriplet([1, 2, 3]))         # True
print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
