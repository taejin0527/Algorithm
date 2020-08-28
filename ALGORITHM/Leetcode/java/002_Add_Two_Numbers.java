/**
 * @FileName : Solution.java
 * @Project : ALGO
 * @Date : 2020. 8. 28
 * @author : "AoN"
 * 
 * @Description : Elementary Math
 * @Link : https://leetcode.com/problems/add-two-numbers/
 * 
 */

/**
 * input
 * [2,4,3]
 * [5,6,4]
 *
 * ouput
 * [7,0,8]
 */

public class Solution {

	public class ListNode {
		int val;
		ListNode next;
		
		ListNode() {}
		ListNode(int val) {	this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode dummyHead = new ListNode(0);
		ListNode p = l1, q = l2;
		ListNode cur = dummyHead;
		
		int carry = 0;
	    while (p != null || q != null) {
	    	int x, y;
	    	if(p != null) {
	    		x = p.val;
	    		p = p.next;
	    	}else {
	    		x = 0;
	    	}
	    	
	    	if(q != null) {
	    		y = q.val;
	    		q = q.next;
	    	}else {
	    		y = 0;
	    	}

	        int sum = carry + x + y;
	        carry = sum / 10;
	        cur.next = new ListNode(sum % 10);
	        cur = cur.next;
	    }
	    if (carry > 0) {
	        cur.next = new ListNode(carry);
	    }
	    return dummyHead.next;
	}
	
	
	static ListNode l1, l2;
	public static void main(String[] args) {
		Solution s = new Solution();
		
		s.addTwoNumbers(l1, l2);
	}
}
