class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];
        if (s.charAt(0) == '0'){
            return 0;
        }
        Arrays.fill(dp, -1);

        return helper(s, 0, s.length()-1, dp);

      //  return ans[0];
    }

    int helper(String s, int start, int end, int[] dp){

        if (start > end){
    
            return 1;
        }

        // 1 char

        if (dp[start] != -1) return dp[start];
        if (s.charAt(start) == '0') return 0;
        int one = helper(s, start + 1, end, dp);


        // 2 chars
        int two = 0;
        if (start != end && Integer.parseInt(s.substring(start,start+2)) < 27){
            two = helper(s, start + 2, end, dp);
        }

        return dp[start] = one + two; 

    }
}

