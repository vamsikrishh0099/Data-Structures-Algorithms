class Solution {
    public int majorityElement(int[] nums) {
        int ans = nums[0];
        int c= 1;

        for (int i = 1; i < nums.length; i++){
            int x = nums[i];
            if (ans == x){
                c++;
            }
            else{
                c--;
            }

            if (c == 0) {
                c= 1;
                ans  = x;
            }
        }

        return ans;
    }


}