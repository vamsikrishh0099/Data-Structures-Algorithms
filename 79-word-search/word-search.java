// class Solution {
//     public boolean exist(char[][] board, String word) {
        
//         // boolean[][] visited = new boolean[board.length][board[0].length];

//         // for (int i = 0;i<board.length;i++){
//         //     for (int j = 0;j<board[0].length;j++){
//         //         for (boolean[] x:visited) Arrays.fill(x,false);
//         //         if (board[i][j] == word.charAt(0)){
//         //             boolean ans = search(board,word.toCharArray(),1,i,j,'0',visited);
//         //             if (ans) return ans;
//         //         }
//         //     }
//         // }
//         // return false;

//     boolean[][] visited = new boolean[board.length][board[0].length];

//     for (int i = 0;i<board.length;i++){
//         for (int j = 0;j<board[0].length;j++){
           

//             if (board[i][j] == word.charAt(0)){
//                 if (dfs(board,word,visited,1,i,j)){
//                     return true;
//                 }
             
//             }
//         }
//     }

//     return false;
        
//     }

//      boolean dfs(char[][] board, String word, boolean[][] visited,int id, int i,int j){

//          if (id == word.length() ) return true;

//         visited[i][j] = true;


//         int[][] moves ={{-1,0},{0,1},{1,0},{0,-1}};

//         for (int k = 0;k<4;k++){
//             int x = i + moves[k][0];
//             int y = j + moves[k][1];
//             if (x >= 0 && x <board.length && y >=0 && y < board[0].length && board[x][y] == word.charAt(id) && !visited[x][y]){
//                 boolean ans = dfs(board,word,visited,id+1,x,y);
//                 if (ans) return ans;
//             }
//         }
//           visited[i][j] = false;

//         return false;

//     }

//     // boolean search(char[][] board, char[] word,int start,int i,int j,char prev,boolean[][] visited){

//         // if (start == word.length) return true;
//         // boolean foundTop = false,foundLeft = false,foundRight = false,foundBottom = false;
//         // visited[i][j] = true;
        
//         // if ( i+1 < board.length && board[i+1][j] == word[start] && !visited[i+1][j]){
            
//         //     foundBottom = search(board,word,start+1,i+1,j,'t',visited);
             
//         // }
//         // if ( i-1 >= 0 && board[i-1][j] == word[start] && !visited[i-1][j]){
            
//         //     foundTop = search(board,word,start+1,i-1,j,'b',visited);
              
//         // }
//         // if ( j+1 < board[0].length && board[i][j+1] == word[start] && !visited[i][j+1]){
            
//         //     foundRight = search(board,word,start+1,i,j+1,'l',visited);
             
            
//         // }
//         // if ( j-1 >= 0 && board[i][j-1] == word[start] && !visited[i][j-1]){
            
//         //     foundLeft = search(board,word,start+1,i,j-1,'r',visited);
              
//         // }
//         // visited[i][j] = false;
//         // return foundBottom || foundTop || foundLeft || foundRight;
        
//     // }
// }


class Solution{
    public boolean exist(char[][] board, String word) {
        int[][] vis = new int[board.length][board[0].length];

        for (int i = 0; i < board.length; i ++){
            for (int j = 0; j < board[0].length;j++){
                for (int[] x: vis) Arrays.fill(x,-1);
                if (board[i][j] == word.charAt(0)){
                    if (dfs(board, vis, i,j,0,word)) return true;
                }
            }
        }

        return false;
    }

    boolean dfs(char[][] board, int[][] vis, int i, int j, int ind, String word){


        if (ind == word.length()-1) return true;

        int[][] dirs = {{0,1},{1,0},{-1,0},{0,-1}};

        vis[i][j] = 1;

        for (int[] dir: dirs){
            int nr = i + dir[0];
            int nc = j + dir[1];

            if (nc >= 0 && nc < board[0].length && nr >= 0 && nr < board.length && 
            vis[nr][nc] != 1 && word.charAt(ind+1) == board[nr][nc]){
                if (dfs(board, vis,nr,nc,ind+1,word)) return true;
            }
        }
        vis[i][j] = 0;
        return false;
    }
}