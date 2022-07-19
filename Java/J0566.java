package Java;

public class J0566 {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        
        int M = mat[0].length;
        int N = mat.length;
        if (M * N != r * c) return mat; // return original if no match

        int row = 0;
        int col = 0;

        int[][] res = new int[r][c]; 
        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M ; j++){
                res[row][col] = mat[i][j];
                col+=1;
                if (col == c) {
                    col = 0;
                    row+=1;
                }
            }
        }
        return res;

    }
}
