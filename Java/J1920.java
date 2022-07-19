package Java;

public class J1920 {
    class Solution {
        public int[] buildArray(int[] nums) {
            int[] ans = new int[nums.length];
            for (int i = 0; i < nums.length; i++) {
                int index = nums[i];
                ans[i] = nums[index];
            }
            return ans;
        }
    }
}
