class Solution {
    public boolean isBipartite(int[][] graph) {
        
        int[] colors = new int[graph.length];

        for (int i = 0; i < graph.length;i++){
            if (colors[i] == 0 && !dfs(i, graph, colors, 1)) return false;
        }

        return true;
    }

    boolean dfs(int node, int[][] graph, int[] colors, int color){

        if (node == graph.length) return true;

        colors[node] = color;

        for (int neigh: graph[node]){
            if (colors[neigh] == 0){
                if (!dfs(neigh, graph, colors, -color)) return false;
            }
            else{
                if (colors[neigh] == color) return false;
            }
        }

        return true;

    }
}