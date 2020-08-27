/**
 * @FileName : 001_Two_Sum.py
 * @Project : LeetCode
 * @Date : 2020-08-27
 * @author : User

 * @Description :
 Approach 1 : Brute Force
 Approach 2 : Two-pass Hash Table
 Approach 3 : One-pass Hash Table
 */

class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();

        s.twoSumBruteForce();
        s.twoSum2PassHash();
        s.twoSum();
    }

     // Approach 1
     // Time complexity : O(n^2)
     // Space complexity = O(1)
    public int[] twoSumBruteForce(int[] nums, int target) {
        for(int i=0; i<nums.length; ++i) {
            for(int j=i+1; j<nums.length; ++j) {
                if(nums[i] + nums[j] == target)
                    return new int[] {i, j};
            }
        }
    }

     // Approach 2
     // Time complexity : O(n)
     // Space complexity = O(n)
    public int[] twoSum2PassHash(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

     }


     // Approach 3
     // Time complexity : O(n^2)
     // Space complexity = O(1)
    public int[] twoSum(int[] nums, int target) {
        for(int i=0; i<nums.length; ++i) {
            for(int j=i+1; j<nums.length; ++j) {
                if(nums[i] + nums[j] == target)
                    return new int[] {i, j};
            }
        }
    }
}