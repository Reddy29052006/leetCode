class Solution:
    def removeStars(self, s: str) -> str:
        t = ''
        i = 0
        while i < len(s):
            if s[i] == '*':
                t = t[:-1]
            else:
                t += s[i]
            i += 1
        return t


solution = Solution()
s = "leet**cod*e"
print(solution.removeStars(s))
