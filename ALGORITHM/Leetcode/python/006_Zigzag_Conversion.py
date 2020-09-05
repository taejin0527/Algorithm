"""
 * @FileName : 006_Zigzag_Conversion.py
 * @Project : LeetCode
 * @Date : 2020. 9. 5.
 * @author : AoN
 * @Link : https://leetcode.com/problems/zigzag-conversion/
 * @Description :
 * 
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        rows = [''] * min(len(s), numRows)
        curRow = 0
        flip = False

        for ch in s:
            rows[curRow] += ch
            if curRow == 0 or curRow == numRows-1:
                flip = not flip
            curRow += 1 if flip else -1

        return ''.join(row for row in rows)