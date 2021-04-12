"""
 * @FileName : 002_Add_Two_Numbers.py
 * @Project : LeetCode
 * @Date : 2020-08-28
 * @author : AoN
 * @Link : https://leetcode.com/problems/add-two-numbers/
 * @Description :
 * 
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()
        cur = dummyHead
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, root = divmod(val1 + val2 + carry, 10)

            cur.next = ListNode(root)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next