/**
 * @FileName :  007_Reverse_Integer.java
 * @Date : 2020. 9. 5.
 * @author : AoN
 * @Link : https://leetcode.com/problems/reverse-integer/
 * @Description : overflow를 어떻게 처리하는지가 핵심인 문제
 *
 */

 class Solution {
      public int reverse(int x) {
        long res = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            x = x / 10;
        }

        if (res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) {
            return 0;
        } else {
            return (int)res;
        }
    }
}