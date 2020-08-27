"""
 * @FileName : 001_Two_Sum.py
 * @Project : LeetCode
 * @Date : 2020-08-27
 * @author : User

 * @Description :
 Approach 1 : Brute Force
 Approach 2 : Two-pass Hash Table
 Approach 3 : One-pass Hash Table

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i in range(len(nums)):
            candidate = target - nums[i]

            if candidate in sum_dict.keys():
                return [i, candidate]


