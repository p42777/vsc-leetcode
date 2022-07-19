package Java;

public class J0028 {
    
    class Solution {
        public int strStr(String haystack, String needle) {
            int ans = 0;
            if (haystack.contains(needle)) {
                ans = haystack.indexOf(needle);
            } 
            else {
                ans = -1;
            }
            return ans;
        }
    }
}
