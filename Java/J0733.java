package Java;

public class J0733 {
    class Solution {
        public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
            if (image[sr][sc] == newColor) return image;
            depthFirstSearch(image, sr, sc, image[sr][sc], newColor);
            return image;
        
        }
        public void depthFirstSearch (int[][] image, int sr, int sc, int color, int newColor){
            if(sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length || image[sr][sc] != color) return;
            image[sr][sc] = newColor;
            depthFirstSearch(image, sr - 1, sc, color, newColor);
            depthFirstSearch(image, sr + 1, sc, color, newColor);
            depthFirstSearch(image, sr, sc + 1, color, newColor);
            depthFirstSearch(image, sr, sc - 1, color, newColor);
        
        }
    }
}