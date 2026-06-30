class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        ans = 0
        n = len(s)
        for r in range(0, n):

            c[s[r]] += 1

            while c['a'] > 0 and c['b'] > 0 and c['c'] > 0:
                c[s[l]] -= 1
                l += 1
                ans += n - r

        return ans


solution = Solution()
print(solution.numberOfSubstrings("abcabc"))
