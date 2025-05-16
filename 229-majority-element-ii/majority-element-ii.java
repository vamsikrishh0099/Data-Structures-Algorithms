class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<>();
        Set<Integer> ans = new HashSet<>();
        int n = nums.length/3;

        for (int x: nums){
            mp.put(x, mp.getOrDefault(x,0) + 1);
           if(mp.get(x) > n & !ans.contains(x)){
            ans.add(x);
           }
        }

        return new ArrayList<>(ans);
    }
}