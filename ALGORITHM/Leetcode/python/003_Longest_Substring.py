"""
 * @FileName : 003_Longest_Substring.py
 * @Project : LeetCode
 * @Date : 2020. 8. 28.
 * @author : AoN
 * @Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * @Description :
 * 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hashMap = {}
        cursor = 0

        for idx, ch in enumerate(s):
            if ch in hashMap:
                cursor = hashMap[ch] if cursor < hashMap[ch] else cursor
            curlen = idx - cursor + 1
            ans = curlen if curlen > ans else ans
            hashMap[ch] = idx + 1

        return ans