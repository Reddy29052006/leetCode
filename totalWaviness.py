from functools import lru_cache


class Solution:

    def solve(self, N: int) -> int:
        if N < 100:
            return 0

        digits = tuple(map(int, str(N)))

        @lru_cache(maxsize=None)
        def dp(pos, prev1, prev2, tight, started):

            if pos == len(digits):
                return (1, 0)

            limit = digits[pos] if tight else 9
            total_numbers = 0
            total_waves = 0

            for d in range(limit + 1):
                new_tight = tight and (d == limit)

                if not started and d == 0:
                    cnt, waves = dp(pos + 1, -1, -1, new_tight, False)
                    total_numbers += cnt
                    total_waves += waves
                else:
                    add_wave = 0
                    if prev2 != -1:
                        if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                            add_wave = 1

                    cnt, waves = dp(pos + 1, d, prev1, new_tight, True)
                    total_numbers += cnt
                    total_waves += waves + cnt * add_wave

            return (total_numbers, total_waves)

        return dp(0, -1, -1, True, False)[1]

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)


s = Solution()

print(s.totalWaviness(132, 1300))
