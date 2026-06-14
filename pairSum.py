from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = node = head
        hold = []
        while node and node.next:
            node = node.next.next
            hold.append(curr.val)
            curr = curr.next

        maxVal = -1
        for i in hold[::-1]:
            i += curr.val
            curr = curr.next
            if i > maxVal:
                maxVal = i
        return maxVal


solution = Solution()
print(solution.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1))))))
