from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi =0
        for i in nums:
            if i == 0:
                if  count > maxi:
                    maxi = count
                count=0
                continue
            count += 1
        if count > maxi:
            maxi = count
        return maxi



obj = Solution()

nums = [1, 1, 0, 1, 1, 1]

result = obj.findMaxConsecutiveOnes(nums)

print(result)