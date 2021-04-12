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
        val = l1.val + l2.val