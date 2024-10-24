class Solution {
    public int minPathSum(int[][] grid) {
        
        int[][] dp = new int[grid.length][grid[0].length];
        for (int[] x:dp) Arrays.fill(x,-1);
       return helper(grid,grid.length-1,grid[0].length-1,dp);

    }


    int helper(int[][] grid,int i,int j,int[][] dp){

        if (i == 0 && j == 0) return grid[i][j];
        if (i<0 || j< 0 ) return 100000;
        if (dp[i][j] != -1) return dp[i][j];

        int top = grid[i][j] + helper(grid,i-1,j,dp);
        int left = grid[i][j] + helper(grid,i,j-1,dp);

        return dp[i][j] = Math.min(top,left);

    }
}