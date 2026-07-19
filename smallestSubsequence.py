class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        print(last)
        stack = []

        for i, ch in enumerate(s):

            if ch in stack:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                stack.pop()

            stack.append(ch)

        return "".join(stack)


solution = Solution()
print(solution.smallestSubsequence("bcabc"))      # abc
# print(solution.smallestSubsequence("cbacdcbc"))   # acdb
