class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> ans = new ArrayList<>();

        boolean[] map = new boolean[nums.length];
        Arrays.fill(map,false);

        helper(nums, map, new ArrayList<Integer>(), ans);
        return ans;

    }

    void helper(int[] nums, boolean[] map, List<Integer> ds, List<List<Integer>> ans){

        if (ds.size() == nums.length){
            ans.add(new ArrayList<>(ds));
            return;
        }

        for (int i = 0;i<nums.length;i++){
            if (!map[i]){
            ds.add(nums[i]);
            map[i] = true;

             helper(nums, map, ds, ans);
            ds.remove(ds.size()-1);
            map[i] = false;
            }

           
            
            
        }
    }
}