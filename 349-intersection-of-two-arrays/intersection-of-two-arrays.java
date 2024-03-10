class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> ans = new HashSet<>();

        Set<Integer> s1 = new HashSet<>();

        for (int x: nums1) s1.add(x);

        for (int x: nums2){
            if (s1.contains(x)){
                ans.add(x);
            }
        }

        int[] fans = new int[ans.size()];

        int i = 0;
        for(int x: ans){
            fans[i] = x;
            i++;
        }

        return fans;
    }
}