from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''

        for i in range(len(strs[0])):
            status = True

            for word in strs[1::]:
                if word == "":
                    status=False
                    break

                if word[i] != strs[0][i]:
                    status=False
                    break

            if not status:
                break

            prefix=prefix+strs[0][i]


        return prefix


obj = Solution()

strs=["abc","","abcd"]

result = obj.longestCommonPrefix(strs)

print(result)