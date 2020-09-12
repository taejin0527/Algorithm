"""
 * @FileName : 008_String_to_Integer_atoi.py
 * @Project : LeetCode
 * @Date : 2020. 9. 12.
 * @author : AoN
 * @Link : 
 * @Description :
 * 
"""

# Approach 1 : Regex
import re


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        pattern = r"^[-+]?[\d]+"
        result = re.findall(pattern, str)

        try:
            if int(result[0]) < -2 ** 31:
                return -2 ** 31
            elif int(result[0]) > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return int(result[0])
        except:
            return 0



# Approach 2 : Scan from left to right
class Solution:
    def myAtoi(self, s: str) -> int:
        num_ch = [str(i) for i in range(10)]
        s = s.strip()
        ret = ''
        if not len(s): return 0
        if s[0] not in num_ch:
            if s[0] in ['-', '+'] and len(s[1:]) and s[1:][0] in num_ch:
                ret += s[0]
                s = s[1:]
            else:
                return 0

        for c in s:
            if not c in num_ch:
                break
            else:
                ret += c
        ret = int(ret)
        if ret < -pow(2, 31):
            return -pow(2, 31)
        if ret > pow(2, 31) - 1:
            return pow(2, 31) -1

        return ret