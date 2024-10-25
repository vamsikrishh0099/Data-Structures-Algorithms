class Solution {
    public int rob(int[] nums) {
       

    //  int[] dp = new int[nums.length+1];
    // dp[0] = nums[0];
    int prev = nums[0];
    int prev2 = 0;
    int ans=prev;


    int pick,nonpick;
    for (int i = 1;i<nums.length;i++){
         nonpick = prev;
        
        pick = prev2 + nums[i];

        ans = Math.max(pick,nonpick);
        prev2 = nonpick;
        prev = ans;
        

    }

    return ans;



        // int[] dp = new int[nums.length];
        // Arrays.fill(dp,-1);
        // return helper(nums,nums.length-1,dp);
        
    }

    // int helper(int[] nums,int i,int[] dp){
     
    //  if (i == 0) return nums[0];

    //  if (i <0 ) return 0;

    // if (dp[i] != -1) return dp[i];

    //  int pick = helper(nums,i-2,dp) + nums[i];
    //  int nonpick = helper(nums,i-1,dp);

    //  dp[i] = Math.max(pick,nonpick);

    //  return dp[i];



    // }
}