"""
 * @FileName : 004_Median_Of_Two_Sorted_Arrays.py
 * @Project : LeetCode
 * @Date : 2020. 8. 28.
 * @author : AoN
 * @Link : https://leetcode.com/problems/median-of-two-sorted-arrays/
 * @Description :
 * 
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_joined = sorted(nums1 + nums2)
        if len(sorted_joined) % 2 == 0:
            index = int(len(sorted_joined) / 2)
            return (sorted_joined[index] + sorted_joined[index-1])/2
        else:
            index = (int(len(sorted_joined)/2))
            return sorted_joined[index]