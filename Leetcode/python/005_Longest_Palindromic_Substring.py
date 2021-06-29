"""
 * @FileName : 005_Longest_Palindromic_Substring.py
 * @Project : LeetCode
 * @Date : 2020. 8. 29.
 * @author : AoN
 * @Link : https://leetcode.com/problems/longest-palindromic-substring/
 * @Description : Manacher Algorithm
 * 
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = ''
        for i in s:
            ss = ss + '#' + i
        ss = ss + '#'
        p = [0] * 2001
        start, end, maxlen, mx = 0, 0, 0, 0

        for i in range(len(ss)):
            p[i] = min(p[2 * id - i], mx - i) if i < mx else 1

            while (i - p[i]) >= 0 and i + p[i] < len(ss) and ss[i - p[i]] == ss[i + p[i]]:
                p[i] += 1

            if mx < i + p[i]:
                id = i
                mx = i + p[i]

            if maxlen < (p[i] - 1):
                maxlen = p[i] - 1
                start = i + 1 - p[i]
                end = i + p[i] - 1

        return ss[start:end + 1].replace('#', '')

s ="babad"
answer = Solution().longestPalindrome(s)