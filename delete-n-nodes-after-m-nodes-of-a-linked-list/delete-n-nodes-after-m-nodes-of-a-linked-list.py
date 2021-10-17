# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # temp = head
        # if temp.next == None:
        #     return head
        # m_count = 1
        # n_count = 1
        # while temp.next != None:
        #     while m_count < m and temp.next != None:
        #         # prev = temp
        #         temp = temp.next
        #         m_count += 1
        #     m_count = 1
        #     if not temp.next:
        #         return head
        #     temp1 = temp.next
        #     while n_count < n and temp.next != None:
        #         temp1 = temp1.next
        #         n_count += 1
        #     n_count = 1
        #     if not temp.next:
        #         return head
        #     temp.next = temp1.next
        #     temp = temp.next
        # return head
        curr = head
        count = 0
        while curr:
            count = 0
            prev = curr
            while count < m and curr:
                prev = curr
                curr = curr.next
                count += 1
            temp = curr
            count = 0
            while count < n and temp:
                temp = temp.next
                count += 1
            if prev:
                prev.next = temp
            curr = temp
        return head