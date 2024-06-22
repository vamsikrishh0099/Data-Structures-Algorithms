class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {


    int[][] visited = new int[obstacleGrid.length][obstacleGrid[0].length];
    for (int[] x: visited) Arrays.fill(x, -1);
    int[] ans = new int[1];
    ans[0] = 0;


    return helper(obstacleGrid, visited, 0,0, ans );
    // return ans[0];

    }

    int helper(int[][] mat, int[][] visited, int i, int j, int[] ans ){


        int m = visited.length;
        int n = visited[0].length;

        if (i == m-1 && j == n-1 && mat[i][j] != 1){
            return 1;
        }

        if (i >= m || j >= n) return 0;
        
        if (visited[i][j] != -1) return visited[i][j];

        if (mat[i][j] == 1 ) return 0;

        int l = helper(mat, visited, i+1, j, ans);
        int r = helper(mat, visited, i, j+1, ans);

        return visited[i][j] = l+r;

        
    }
}