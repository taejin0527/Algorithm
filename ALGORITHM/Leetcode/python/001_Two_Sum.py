"""
 * @FileName : 001_Two_Sum.py
 * @Project : LeetCode
 * @Date : 2020-08-27
 * @author : User

 * @Description : java 파일에서 3가지 방법을 모두 보였음으로 최적의 방법만 메모
 * --> One-pass Hash Table

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in sum_dict:
                return sum_dict[complement], i
            sum_dict[num] = i

