/**
 * @FileName : 004_Median_Of_Two_Sorted_Arrays.py
 * @Project : LeetCode
 * @Date : 2020. 8. 28.
 * @author : AoN
 * @Link : https://leetcode.com/problems/median-of-two-sorted-arrays/
 * @Description :
 *
 */

public class Solution() {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalLen = nums1.length + nums2.length;
        int maxStep = totalLen >> 1;
        int smaller = 0, bigger = 0;

        for (int i = 0, i1 = 0, i2 = 0; i <= maxStep; i++) {
            if (i1 >= nums1.length) {
                smaller = bigger;
                bigger = nums2[i2++];
            } else if (i2 >= nums2.length) {
                smaller = bigger;
                bigger = nums1[i1++];
            } else {
                if (nums1[i1] < nums2[i2]) {
                    smaller = bigger;
                    bigger = nums1[i1++];
                } else if (nums1[i1] == nums2[i2]) {
                    if (++i <= maxStep) {
                        smaller = nums1[i1++];
                        bigger = nums2[i2++];
                    } else {
                        bigger = nums1[i1];
                        break;
                    }
                } else {
                    smaller = bigger;
                    bigger = nums2[i2++];
                }
            }
        }

        return ((totalLen & 1) != 1) ? (double) (smaller + bigger) / 2 : bigger;
    }
}