

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        if (color == image[sr][sc]) return image;
       int org =  image[sr][sc];
       image[sr][sc] = color;

        Queue<int[]> q = new LinkedList<>();

        int[] p = new int[]{sr,sc};
        q.offer(p);
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        while(!q.isEmpty()){
            int[] cur = q.poll();

            for (int i = 0 ; i < 4; i ++){
                int r = cur[0] + dirs[i][0];
                int c = cur[1] + dirs[i][1];

                if (r >= 0 && r < image.length && c >= 0 && c < image[0].length && image[r][c] != color && image[r][c] == org){
                    q.offer(new int[]{r,c});
                    image[r][c] = color;
                }
            }
        }

        return image;
    }
}