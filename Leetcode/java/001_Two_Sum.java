/**
 * @FileName : TwoSum.java
 * @Project : ALGO
 * @Date : 2020. 8. 28 
 * @author : "AoN"
 * @Link : https://leetcode.com/problems/two-sum/
 * @Description : Brute-force, Two-pass hashmap, One-pass hashmap
 * 
 */

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	
	static int[] nums = new int[] {2, 7, 11, 15};
	static int target = 9; 
	
	public static void main(String[] args) {
        TwoSum s = new TwoSum();

        s.twoSumBruteForce(nums, target);
        s.twoSum2PassHash(nums, target);
        s.twoSum(nums, target);
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
        throw new IllegalArgumentException("No Two sum solution");
    }

     // Approach 2
     // Time complexity : O(n)
     // Space complexity = O(n)
    public int[] twoSum2PassHash(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<nums.length; ++i) {
            map.put(nums[i], i);
        }
        for(int i=0; i<nums.length; ++i) {
            int complement = target - nums[i];
            if(map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { i, map.get(complement)};
            }
        }
        throw new IllegalArgumentException("No Two sum solution");
     }


     // Approach 3
     // Time complexity : O(n^2)
     // Space complexity = O(1)
    public int[] twoSum(int[] nums, int target) {
    	Map<Integer, Integer> map = new HashMap<>();
    	
    	for(int i=0; i<nums.length; ++i) {
    		int complement = target - nums[i];
    		if(map.containsKey(complement)) {
    			return new int[] { i, map.get(complement) };
    		}
    		map.put(nums[i], i);
    	}
        throw new IllegalArgumentException("No Two sum solution");
    }
}
