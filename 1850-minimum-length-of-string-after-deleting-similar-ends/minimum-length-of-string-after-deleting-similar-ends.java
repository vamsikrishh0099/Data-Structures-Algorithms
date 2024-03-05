class Solution {
    public int minimumLength(String s) {
        
        int l = 0;
        int h = s.length()-1;

        while (l <= h){
            if (l == h) return 1;
            if (s.charAt(l) == s.charAt(h)){
                while (s.charAt(l) == s.charAt(l+1) && l+1 <h){
                    l++;
                }

                while (s.charAt(h) == s.charAt(h-1) && h > l){
                    h--;
                }
                l++;
                h--;

            }
            else{
                return h - l+1;
            }
        }

        return 0;

    }
}