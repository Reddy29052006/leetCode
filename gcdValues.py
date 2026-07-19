from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        MAX = max(nums)

        # Frequency of each number
        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (MAX + 1)
        for d in range(1, MAX + 1):
            for multiple in range(d, MAX + 1, d):
                cnt[d] += freq[multiple]

        exact = [0] * (MAX + 1)

        for d in range(MAX, 0, -1):
            pairs = cnt[d] * (cnt[d] - 1) // 2

            multiple = 2 * d
            while multiple <= MAX:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        prefix = []
        gcdValue = []

        total = 0
        for d in range(1, MAX + 1):
            if exact[d]:
                total += exact[d]
                prefix.append(total)
                gcdValue.append(d)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcdValue[idx])

        return ans
