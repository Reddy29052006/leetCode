class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.strip().split()[::-1])
        return s


s = Solution()
st = "    the sky is      blue     "

print(s.reverseWords(st))
