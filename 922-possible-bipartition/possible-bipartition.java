class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {

        int[] colors = new int[n+1];
        Arrays.fill(colors,-1);
 
        List<List<Integer>> g = new ArrayList<>();
        for (int i = 0 ; i < n+1; i ++){
            g.add(new ArrayList<>());
        }

        for (int[] pair: dislikes){
            g.get(pair[0]).add(pair[1]);
            g.get(pair[1]).add(pair[0]);
        }

        for (int i = 1; i < n+1; i++){
            if(colors[i] == -1){
                if (bfs(i, n, g, colors) == false) return false;
            }
        }
        return true;

    }

    boolean bfs(int start, int n, List<List<Integer>> g,  int[] colors){

        Queue<Integer> q = new LinkedList<>();
        
        colors[start] = 0;
        q.offer(start);

        while (!q.isEmpty()){
            int node = q.poll();

            for (int neigh: g.get(node)){
                if (colors[neigh] == -1){
                    colors[neigh] = 1 - colors[node];
                    q.offer(neigh);
                }
                else{
                    if (colors[neigh] == colors[node]) return false;
                }
            }
        }

        return true;
    }



    // boolean check(int node, Map<Integer, List<Integer>> g, int  colors, int[] marked, int n){

    //     if (node == n+1){
    //         return true;
    //     }

    //     for (int color = 1; color <= colors; color++){

    //         if (!g.containsKey(node) || checkColor(node, g, color, marked)){
    //             marked[node] = color;
    //             if (check(node+1, g, 2, marked, n) == true) return true;
    //             marked[node] = 0;
    //         }
    //     }

    //     return false;
    // }

    // boolean checkColor(int node,  Map<Integer, List<Integer>> g, int color, int[] marked){

    //     for (int neigh: g.get(node)){
    //         if (marked[neigh] == color) return false;
    //     }

    //     return true;
    // }

}