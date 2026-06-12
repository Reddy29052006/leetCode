class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)
        dp = [False] * n
        dp[0] = True            # ← always start here

        for i in range(n):
            if dp[i]:           # ← only expand reachable indexes
                for j in range((i+minJump),min(i+maxJump,n-1)+1):   # ← you fill this!
                    if s[j] == '0':
                        dp[j] = True

        return dp[n-1]

s ="01010101001010"

obj = Solution()
result = obj.canReach(s,2,3)

print(result)