"""
 * @FileName : 007_Reverse_Integer.py
 * @Project : LeetCode
 * @Date : 2020. 9. 5.
 * @author : AoN
 * @Link : https://leetcode.com/problems/reverse-integer/
 * @Description :
 * 
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:  # handle positive numbers
            ret = int(str(x)[::-1])
        if x <= 0:  # handle negative numbers
            ret = -1 * int(str(x * -1)[::-1])

        # handle 32 bit overflow
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1

        return ret if ret < min_val or ret > max_val else 0