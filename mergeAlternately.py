class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergeStr = []
        count = 0

        while count < len(word1) or count < len(word2):
            if count < len(word1):
                mergeStr.append(word1[count])
            if count < len(word2):
                mergeStr.append(word2[count])
            count += 1

        return "".join(mergeStr)


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
print(s.mergeAlternately("ab", "pqrs"))
print(s.mergeAlternately("abcd", "pq"))
