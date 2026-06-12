
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = self.gcd(len(str1), len(str2))

        return str1[:length]

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a


str1 = "ABABAB"
str2 = "ABAB"


s = Solution()
print(s.gcdOfStrings(str1=str1, str2=str2))
