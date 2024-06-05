class Solution {
    public List<String> commonChars(String[] words) {
        Map<String, Map<Character, Integer>> wordsMap = new HashMap<>();
        List<String> ans = new ArrayList<>();

        for (String s: words){
            Map<Character, Integer> freq = new HashMap<>();

            for (int i = 0; i < s.length();i++){
                char c = s.charAt(i);
                freq.put(c, freq.getOrDefault(c, 0)+1);
            }
            wordsMap.put(s,freq);
        }

        for (char c: wordsMap.get(words[0]).keySet()){
            boolean isCommon = true;
            int minFreq = Integer.MAX_VALUE;
            for (int j = 0; j < words.length;j++){
                String word = words[j];
                if (!wordsMap.get(word).containsKey(c)){
                    isCommon = false;
                    break;
                }
                minFreq = Math.min(minFreq, wordsMap.get(word).get(c));

            }
            if (!isCommon) continue;

            for (int k = 0; k < minFreq;k++){
                ans.add(Character.toString(c));
            }
        }

        //for (int i = 0; i < wordsMap.get(words[0]).size();i++){
           // char c = words[0].charAt(i);
            // boolean isCommon = true;
            // int minFreq = Integer.MAX_VALUE;
            // for (int j = 0; j < words.length;j++){
            //     String word = words[j];
            //     if (!wordsMap.get(word).containsKey(c)){
            //         isCommon = false;
            //         break;
            //     }
            //     minFreq = Math.min(minFreq, wordsMap.get(word).get(c));

            // }
            // if (!isCommon) continue;

            // for (int k = 0; k < minFreq;k++){
            //     ans.add(Character.toString(c));
            // }
        //}

        return ans;
    }
}