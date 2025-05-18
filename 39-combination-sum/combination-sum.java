class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();

        //  func(candidates,0,target,ans,new ArrayList<>());
        func2(candidates, 0, target, new ArrayList<>(), ans);

        return ans;
    }

    void func2(int[] candidates, int ind, int target, List<Integer> cur, List<List<Integer>> ans) {

        if (target == 0) {
            ans.add(new ArrayList<>(cur));
            return;
        } else if (target < 0 || ind == candidates.length) {
            return;
        }

        cur.add(candidates[ind]);
        func2(candidates, ind, target - candidates[ind], cur, ans);
        cur.remove(cur.size() - 1);

        func2(candidates, ind + 1, target, cur, ans);

    }

    void func(int[] nums, int ind, int target, List<List<Integer>> ans, List<Integer> cur) {

        if (ind == nums.length) {
            if (target == 0) {
                ans.add(new ArrayList<Integer>(cur));
            }
            return;
        }

        if (nums[ind] <= target) {
            cur.add(nums[ind]);
            func(nums, ind, target - nums[ind], ans, cur);
            cur.remove(cur.size() - 1);

        }
        func(nums, ind + 1, target, ans, cur);

    }

}