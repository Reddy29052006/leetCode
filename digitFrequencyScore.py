class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sum = 0
        while n:
            sum += n % 10
            n = n//10
        return sum


s = Solution()
print(s.digitFrequencyScore(122))
