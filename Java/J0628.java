package Java;

import java.util.Arrays;

public class J0628 {
    class Solution {
        public int maximumProduct(int[] nums) {
            Arrays.sort(nums);
            int productL = nums[0] * nums[1] * nums[nums.length - 1];
            int productR = nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3];
            return Math.max(productL, productR);
        }
    }
}
