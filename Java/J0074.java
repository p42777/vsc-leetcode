package Java;

public class J0074 {
    
    class Solution {
        public boolean searchMatrix(int[][] matrix, int target) {
            int m = matrix.length;
            int n = matrix[0].length;
            int l = 0;
            int r = n * m - 1;

            // Binary Search
            while(l <= r){
                int i = ( l + r ) / 2;
                int row = i / n;
                int col = i - n * row;
                int val = matrix[row][col];
                if(target > val){
                    l = i + 1;
                }
                else if(target < val){
                    r = i - 1;
                }
                else{
                    return true;
                }

            }
   
            return false;

        }
    }
    
}
