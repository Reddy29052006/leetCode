class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelsString = []
        s = list(s)

        for ltr in s:
            if ltr.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowelsString.append(ltr)

        j = len(vowelsString) - 1

        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                s[i] = vowelsString[j]
                j -= 1

        return ''.join(s)


s = Solution()
print(s.reverseVowels("IceCreAm"))
