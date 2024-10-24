class Solution {
    public int minPathSum(int[][] grid) {
        
        int[][] dp = new int[grid.length][grid[0].length];

        for (int[] x: dp) Arrays.fill(x, -1);

        helper(grid, 0, 0, dp);

        return dp[0][0];

    }

    int helper(int[][] grid, int i, int j, int[][] dp){

        if (i == grid.length-1 && j == grid[0].length-1){
            return dp[i][j] = grid[i][j];
        }

        if (i >= grid.length || j >= grid[0].length){
            return 100000000;
        }

        if (dp[i][j] != -1) return dp[i][j];

        int d = grid[i][j] + helper(grid, i + 1, j, dp);
        int r = grid[i][j] + helper(grid, i, j+1, dp);

        return dp[i][j] = Math.min(d,r);
    }
}