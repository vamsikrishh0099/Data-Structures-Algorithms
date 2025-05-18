class Solution {
    public List<List<String>> solveNQueens(int n) {
        
        List<List<String>> ans = new ArrayList<>();

        int[][] board = new int[n][n];

        for (int[] x: board) Arrays.fill(x,0);

        helper(board,new ArrayList<String>(), ans, 0,0);

        return ans;
    }

    void helper(int[][] board, List<String> ds, List<List<String>> ans, int placed, int rowNum){

        if (ds.size() == board.length){
            ans.add(new ArrayList<>(ds));
            return;
        }

        for (int row = rowNum;row<board.length;row++){
            char[] pos = new char[board.length];
            Arrays.fill(pos,'.');
            boolean valid = false;
            for (int col = 0; col < board.length;col++){
                if (board[row][col] == 0){
                    valid = true;
                    pos[col] = 'Q';
                    ds.add(new String(pos));
                    board[row][col] = 1;
                    mark(row,col,board,1);
                    helper(board,ds,ans,placed+1,row+1);
                    ds.remove(ds.size()-1);
                    mark(row,col,board,-1);
                    board[row][col] = 0;
                    pos[col] = '.';
                }
            }
            if (!valid) return;

        }
    }

    void mark(int row, int col, int[][] board,int val){
       
       // fill rows
         for (int i = 0;i<board.length;i++){
           if (i!=col) board[row][i] += val; 
       }

       //fill cols
       for (int i = 0;i<board.length;i++){
           if (i!=row) board[i][col] += val; 
       }
       int temprow = row;
       int tempcol = col;

       // fill diag
           //top left
           while (row-1 >= 0 && col-1 >=0){
               row = row-1;
               col = col-1;
               board[row][col] += val;
           }
           row = temprow;
           col = tempcol;

            //top right
           while (row-1 >= 0 && col+1 < board.length){
               row = row-1;
               col = col+1;
               board[row][col] += val;
           }
           row = temprow;
           col = tempcol;

             //bottom left
           while (row+1 < board.length && col-1 >= 0){
               row = row+1;
               col = col-1;
               board[row][col] += val;
           }
           row = temprow;
           col = tempcol;

                //bottom right
           while (row+1 < board.length && col+1 <board.length){
               row = row+1;
               col = col+1;
               board[row][col] += val;
           }
       
    }
}