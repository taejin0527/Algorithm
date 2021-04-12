"""
 * @FileName : 003_Longest_Substring.java
 * @Project : LeetCode
 * @Date : 2020-08-28
 * @author : AoN
 * @Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * @Description : HashMap을 활용해서 커서를 한 번에 이동하는 방식은 복습해서 외우도록 하자
 *
"""

class Solution {

    // Approach 1 : Brute Force (완전 탐색)
    // Time complexity : O(n^3)
    // Space complexity : O(min(n, m)) <- 집합의 크기
    public int lengthOfLongestSubstring(String s) {
        int sLen = s.length();
        int ans = 0;

        for(int i=0; i<sLen; ++i)
            for(int j=i+1; j<=sLen; ++j)
                if(allUnique(s, i, j)) ans = Math.max(ans, j-i);

        return ans;
    }

    private boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();

        for(int i=start; i<end; ++i) {
            char ch = s.charAt(i);
            if (set.contains(ch)) return false;
            set.add(ch);
        }
        return true;
    }

    // Approach 2 : Sliding Window (using HashSet)
    // Time complexity : O(2n) = O(n)
    // Space complexity : O(min(n, m)) <- 집합의 크기
    public int lengthOfLongestSubstring(String s) {
        int sLen = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, left = 0, right = 0;

        while(left < sLen && right < sLen) {
            if(!set.contains(s.chartAt(right))) {
                set.add(s.chartAt(right++));
                ans = Math.max(ans, right - left);
            }else{
                set.remove(s.chartAt(left++));
            }
        }
        return ans;
    }

    // Approach 3 : Sliding Window (using HashMap)
    // Time complexity : O(n)
    // Space complexity : O(min(n, m)) <- 집합의 크기
     public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
}