class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] cumsum = new int[words.length];
        int[] ans = new int[queries.length];
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        if (vowels.contains(words[0].charAt(0)) && vowels.contains(words[0].charAt(words[0].length()-1))){
            cumsum[0] = 1;
        }
        for (int i = 1; i < words.length; i++){
            String s = words[i];
            if (vowels.contains(s.charAt(0)) && vowels.contains(s.charAt(s.length()-1))){
                cumsum[i] = cumsum[i-1] + 1;
            }
            else{
                cumsum[i] = cumsum[i-1];
            }
        }

        for (int i = 0 ; i < queries.length; i++){
            int[] query = queries[i];
            int l = query[0];
            int r = query[1];
            if (l == 0){
                ans[i] = cumsum[r];
            }
            else{
                ans[i] = cumsum[r] - cumsum[l-1];
            }
            
            
        }

        return ans;
    }
}