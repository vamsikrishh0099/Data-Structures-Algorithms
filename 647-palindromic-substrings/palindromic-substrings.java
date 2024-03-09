class Solution {
    public int countSubstrings(String s) {

        int l = 0;
        int r = 0;
        int ans = 0;

        for (int i = 0; i < s.length(); i++) {
            l = i;
            r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {

                ans += 1;
                l--;
                r++;

            }

            l = i;
            r = i + 1;

            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {

                ans += 1;
                l--;
                r++;

            }

        }

        return ans;

    }
}