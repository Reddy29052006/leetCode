from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        less = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                greater.insert(0, num)
            else:
                greater.append(num)

        return less + greater


solution = Solution()
print(solution.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
