class Solution {
    public int maxMoves(int[][] grid) {
        
        
        int[][] dp = new int[grid.length][grid[0].length];
        for (int[] x: dp) Arrays.fill(x, -1);
         int ans = 0;
        for (int i = 0; i < grid.length; i++){
            ans = Math.max(ans, helper(grid, i,0, dp));
        }
        return ans; 

    }

    int helper(int[][] grid, int i, int j, int[][] dp){


        int[][] moves = {{-1,1}, {0,1}, {1,1}};

        if (dp[i][j] != -1) return dp[i][j];
        
        int ans = 0;
        int val = grid[i][j];

        for (int[] move: moves){
            int x = i + move[0];
            int y = j + move[1];

            if (x < grid.length && y < grid[0].length && x >= 0 && y >= 0 && val < grid[x][y]){
                
                
                ans = Math.max(1 + helper(grid, x, y, dp), ans);
            }
        }

        return dp[i][j] = ans;
    }
}
