from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
                 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        for word in words:
            sum = 0
            for char in word:
                sum += weights[alpha[char]]

            res.append(chr(122-sum % 26))

        return "".join(res)


words = ["abcd", "def", "xyz"]
weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6,
           9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]

solution = Solution()
print(solution.mapWordWeights(words, weights))
