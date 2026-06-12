from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        expectedNums =[]
        for num in nums:
            if num == val:
                expectedNums.insert(0, num)
                count += 1
                continue
            expectedNums.append("_")

        return  expectedNums, count


obj = Solution()

nums = [3,2,2,3]
val = 3

result = obj.removeElement(nums,val)

print(result)