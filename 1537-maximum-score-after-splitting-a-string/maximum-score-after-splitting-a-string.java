class Solution {
    public int maxScore(String s) {
        int ans = -1;
        int z = 0;
        int o = 0;

        for (int i = 0; i < s.length(); i ++){
            if (s.charAt(i) == '1') o++;
        }

        for (int i = 0; i < s.length()-1; i ++ ){
            char c = s.charAt(i);

            if (c == '0' ){
                z++;
                
            }
            else{
                o--;
            }

            ans = Math.max(ans, z + o);
        }

        return ans;
    }
}