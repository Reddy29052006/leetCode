from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()

        c = 1
        j = 0

        if 1 in freq[1]:
            c = freq[1] if freq[1] % 2 != 2 else freq[1]-1

        for num, count in freq.items():
            if num == 1:
                continue
            if count == 2 and num**c in freq:
                c += 1
            j = max(j, c)


solution = Solution()
nums = [5, 4, 1, 2, 2]
print(solution.maximumLength(nums))
