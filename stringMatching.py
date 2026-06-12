from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        matchingWords = []
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    matchingWords.add(words[i])

                if words[j] in words[i]:
                    matchingWords.add(words[j])

        return matchingWords


obj = Solution()

words = ["neetcode", "neeet", "neet", "code"]

result = obj.stringMatching(words)

print(result)
