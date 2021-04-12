/**
 * @FileName :  006_Zigzag_Conversion.java
 * @Project : LeetCode
 * @Date : 2020. 9. 5.
 * @author : AoN
 * @Link : https://leetcode.com/problems/zigzag-conversion/
 * @Description :
 *
 */

// Approach 1 : 지그재그 모양을 그려가는 방법(위 아래로 왕복)
class Solution {
    public String convert(String s, int numRows) {
        // 지그재그가 없는 경우
        if(numRows == 1) return s;

        List<StringBuilder> rows = new ArrayList<>();
        // 문자열 s의 길이가 행의 수보다 작을 수 있기 때문에 둘 중 최소값만큼 공간을 확보한다
        for (int i=0; i<Math.min(s.length(), numRows); ++i) {
            rows.add(new StringBuilder());
        }

        int curRow = 0;
        boolean flip = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);

            if(curRow == 0 || curRow == numRows - 1) flip = !flip;
            curRow += flip ? 1 : -1;
        }

        StringBuilder ret = new StringBuilder();
        for (StringBuilder row : rows) ret.append(row);

        return ret.toString();
    }
}

// Approach 2 : 비슷한데 가로로 진행한다
class Solution {
    public String convert(String s, int numRows) {

        if (numRows == 1) return s;

        StringBuilder ret = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret.append(s.charAt(j + cycleLen - i));
            }
        }
        return ret.toString();
    }
}