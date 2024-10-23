class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];

       return helper(s,0,s.length()-1,dp);
    }


    int helper(String s,int start,int end,int[] dp){
        
         if (start == end+1) return 1;

         if (dp[start]!=0) return dp[start];
         char c= s.charAt(start);
               if (c == '0') return 0;
        if (start == end) return 1;
       
        int one = helper(s,start+1,end,dp);
     
    if (Integer.valueOf(s.substring(start,start+2)) < 27){
              one += helper(s,start+2,end,dp);
        }
       
        return dp[start] = one;
    }
}