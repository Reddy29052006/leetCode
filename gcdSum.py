class Solution:
    def gcd(self, a, b) -> int:
        while b != 0:
            a, b = b, a % b

        return a

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        temp = 0

        for num in nums:
            if temp <= num:
                temp = num

            prefixGcd.append(self.gcd(temp, num))

        prefixGcd.sort()
        sum = 0
        i = 0
        j = len(prefixGcd)-1

        while (i < j):
            print(f"{i}:{prefixGcd[i], prefixGcd[j]}")
            sum += self.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return sum


solution = Solution()
nums = [3, 6, 2, 8]

print(solution.gcdSum(nums))
