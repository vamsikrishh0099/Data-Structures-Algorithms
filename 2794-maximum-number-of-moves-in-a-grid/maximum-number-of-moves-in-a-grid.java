class Solution {
    public int maxMoves(int[][] grid) {
        
        int[][] visited = new int[grid.length][grid[0].length];

        int ans = 0;
        for (int i = 0; i < grid.length; i++){
            ans = Math.max(ans, helper(grid, i,0,visited));
        }
        return ans; 

    }

    int helper(int[][] grid, int i, int j, int[][] vis){


        int[][] moves = {{-1,1}, {0,1}, {1,1}};

        vis[i][j] = 1;
        int ans = 0;
        int val = grid[i][j];

        for (int[] move: moves){
            int x = i + move[0];
            int y = j + move[1];

            if (x < grid.length && y < grid[0].length && x >= 0 && y >= 0 && vis[x][y] != 1 && val < grid[x][y]){
                
                ans = Math.max(1 + helper(grid, x, y, vis), ans);
            }
        }

        return ans;
    }
}
