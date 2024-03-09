class Solution {
    public int longestCommonSubsequence(String text1, String text2) {

        int[][] mem = new int[text1.length()+1][text2.length()+1];
        for (int[] x:mem){
            Arrays.fill(x,-1);
        }
        return helper2(text1,text2,text1.length()-1,text2.length()-1,mem);
        
    }

    int helper(String s1, String s2,int i1,int i2,int[][] mem){

        if (i1<0 || i2<0){
            return 0;
        }

        if (mem[i1+1][i2+1]!=-1){
            return mem[i1+1][i2+1];
        }

        if (s1.charAt(i1) == s2.charAt(i2)){
            mem[i1+1][i2+1] = 1 + helper(s1,s2,i1-1,i2-1,mem);

            return  mem[i1+1][i2+1];
        }

       mem[i1+1][i2] = helper(s1,s2,i1,i2-1,mem);
            mem[i1][i2+1] = helper(s1,s2,i1-1,i2,mem);

        return Math.max( mem[i1+1][i2], mem[i1][i2+1]);

    }

    int helper2( String s1, String s2, int i1, int i2, int[][] dp){


        if (i1 < 0 || i2 < 0 ){
            return 0;
        }

        if (dp[i1][i2] != -1) return dp[i1][i2];

        if (s1.charAt(i1) == s2.charAt(i2)){
            return dp[i1][i2] = 1 + helper2(s1,s2,i1-1,i2-1,dp);
        }
      
            int l = helper2(s1,s2,i1-1,i2,dp);
            int r = helper2(s1,s2,i1,i2-1,dp);
            return dp[i1][i2] = Math.max(l,r);
        
    }
}