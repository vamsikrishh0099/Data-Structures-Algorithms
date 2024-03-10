class Solution {
    public String countAndSay(int n) {
        

        if (n == 1) return "1";

        String s = countAndSay(n-1);
        return convert(s);
    }

    String convert(String s){
  
        StringBuilder ans = new StringBuilder();

        int start = 0;
        int end = 0;

        while(end < s.length()){
            int charCount = 0;
            while(end < s.length() && s.charAt(start) == s.charAt(end)){
                end++;
                charCount++;
            }
            ans.append(charCount);
            ans.append(s.charAt(start));
            start = end;

        }


        return ans.toString();
    }
}