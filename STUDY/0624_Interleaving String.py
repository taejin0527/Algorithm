"""
 * @FileName : 0624_Interleaving String.py
 * @Project : LeetCode
 * @Date : 2021-06-24
 * @author : AoN
 * @Link :
 * @Description :
 * 
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i: int, j: int, k: int, found: bool) -> bool:
            if memo[i][j]:
                return False
            memo[i][j] = True

            if k == len(s3):
                found = True
            if found:
                return found

            if i < len(s1) and s1[i] == s3[k]:
                found = dfs(i + 1, j, k + 1, found)
            if j < len(s2) and s2[j] == s3[k]:
                found = dfs(i, j + 1, k + 1, found)

            return found

        answer = dfs(0, 0, 0, False)
        print(answer)

        return answer


# s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"


ans = Solution().isInterleave(s1, s2, s3)
