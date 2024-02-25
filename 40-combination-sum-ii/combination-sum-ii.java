class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        
       // Set<List<Integer>> ans = new HashSet<>();
        List<List<Integer>> ans = new ArrayList<>();

        Arrays.sort(candidates);

        helper2(candidates,0,target,new ArrayList<Integer>(), ans);
        
        return new ArrayList<>(ans);
    }

    void helper2(int[] candidates, int ind, int target, List<Integer> cur, List<List<Integer>> ans){

        if (target < 0 ){
            return;
        }
        if (target == 0){
            ans.add(new ArrayList<>(cur));
        return;
        }

       for (int i = ind; i < candidates.length;i++){

           if (i != ind && candidates[i] == candidates[i-1]){
               continue;
           }
        cur.add(candidates[i]);
        helper2(candidates, i + 1, target - candidates[i], cur, ans);
        cur.remove(cur.size()-1);


       }
        
       

    }

    void helper(int[] candidates, int index, int target, List<Integer> cur, Set<List<Integer>> ans){

        
            if (target==0){
                ans.add(new ArrayList<>(cur));
            }
      
        

        for (int i = index;i<candidates.length;i++){
            if (i > index && candidates[i] == candidates[i-1]){
                continue;
            }
            if (candidates[i] > target) break;

            cur.add(candidates[i]);
            helper(candidates,i+1,target-candidates[i],cur,ans);
            cur.remove(cur.size()-1);
        }

    

    }
}