from typing import List


class Solution:
    def maxOperations(self, nums, k):
        freq = {}
        operations = 0

        for num in nums:
            target = k - num

            if freq.get(target, 0) > 0:
                freq[target] -= 1
                operations += 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return operations


solution = Solution()
nums = [1, 2, 3, 4]
k = 5

print(solution.maxOperations(nums, k))
