from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        while read < n:
            count = 0
            cur = chars[read]

            while read < n and cur == chars[read]:
                read += 1
                count += 1

            chars[write] = cur
            write += 1

            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1

        return write


chars = ["a", "a", "b", "b", "c", "c", "c"]

s = Solution()
length = s.compress(chars)

print(length)
print(chars[:length])
