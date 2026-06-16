class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for ch in s:
            if ch == '*':
                res = res[:-1]
            elif ch == '#':
                res += res
            elif ch == '%':
                res = res[::-1]
            else:
                res += ch

        return res


solution = Solution()
s = "a#b%*"

print(solution.processStr(s))
