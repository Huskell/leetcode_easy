#Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 and not l2: return
        if not l1: return l2
        if not l2: return l1

        root = ListNode(0)
        curr = root

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next

        if not l1: curr.next = l2
        if not l2: curr.next = l1

        return root.next



if __name__ == '__main__':
    l1_3 = ListNode(4)
    l1_2 = ListNode(2)
    l1_2.next = l1_3
    l1_1 = ListNode(1)
    l1_1.next = l1_2
    l1 = l1_1

    l2_3 = ListNode(4)
    l2_2 = ListNode(2)
    l2_2.next = l1_3
    l2_1 = ListNode(1)
    l2_1.next = l2_2
    l2 = l2_1
    sol = Solution().mergeTwoLists(l1, l2)
    print(sol)