class Solution {
   public String longestPalindrome(String s) {
	
    int len = 0;
    String ans = "";
    int l = 0;
    int r = 0;

    for (int i = 0 ; i < s.length();i++){
         l = i;
         r = i;
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            if (len < r-l+1){
            ans = s.substring(l,r+1);
            len = r - l+1;
        }
            l--;
            r++;

        }

        

    }

    for (int i = 0 ; i < s.length();i++){
         l = i;
         r = i+1;
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            if (len < r-l+1){
            ans = s.substring(l,r+1);
            len = r - l+1;
        }
            l--;
            r++;

        }

        

    }

    return ans;
}

}