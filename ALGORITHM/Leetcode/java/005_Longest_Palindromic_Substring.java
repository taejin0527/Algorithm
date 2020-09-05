/**
 * @FileName :  005_Longest_Palindromic_Substring.java
 * @Project : LeetCode
 * @Date : 2020. 8. 29.
 * @author : AoN
 * @Link : https://leetcode.com/problems/longest-palindromic-substring/
 * @참고 : https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
 *
 */

// Approach 1 : Dynamic Programming
 class Solution {
   public String longestPalindrome(String s) {
	   int len = s.length();
	   char[] c = s.toCharArray();
	   Boolean[][] dp = new Boolean[len][len];
	   int start = 0, end = 0;

	   for (int i= len-1; i>= 0; i--) {
		   for (int j = i; j<len; j++) {
               if (j-i < 3) { //base case
                 dp[i][j] = (c[i] == c[j]);
               } else {
                  dp[i][j] = (c[i] == c[j] && dp[i+1][j-1]);
               }

			   if (dp[i][j] && (end-start <= j-i)) {
				   start = i;
				   end = j;
			   }
		   }
	   }
	   return s.substring(start, end+1);
   }
}