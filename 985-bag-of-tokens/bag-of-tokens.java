class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {

        int[] ans = new int[1];
        int[] vis = new int[tokens.length];
        Arrays.sort(tokens);

        helper(tokens, power, vis, ans, 0, 0, 0, tokens.length - 1);

        return ans[0];

    }

    void helper(int[] tokens, int power, int[] vis, int[] ans, int used, int score, int l, int h) {

        ans[0] = Math.max(ans[0], score);

        if (l> h) return;

        if (power >= tokens[l]) {
        
            while (vis[l] == 1) {
                l++;
                if (l >= h)
                    break;
            }
            if (l < tokens.length && l <= h) {
                vis[l] = 1;
                helper(tokens, power - tokens[l], vis, ans, used + 1, score + 1, l + 1, h);
            }

        } else if(score >= 1) {
            while (vis[h] == 1) {
                h--;
                if (h <= l)
                    break;
            }
            if (h > 0 && h >=l) {
                  vis[h] = 1;
            helper(tokens, power + tokens[h], vis, ans, used + 1, score - 1, l, h - 1);
            }
        }


    }

}