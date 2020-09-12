"""
 * @FileName : 009_Palindrome_Number.py
 * @Project : LeetCode
 * @Date : 2020. 9. 12.
 * @author : AoN
 * @Link : 
 * @Description :
 * 
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])