class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        
        List<String> ans = new ArrayList<>();
        int i = 0;
        while (i < words.length ){
            List<String> cur = getWords(words, i, maxWidth);
            i += cur.size();
            ans.add(getCurrentLine(words, i, cur, maxWidth));
        }

        return ans;
    }

    List<String>  getWords(String[] words, int i, int maxWidth){
        int curLength = 0;
        List<String> cur = new ArrayList<>();
        while (i < words.length && curLength + words[i].length() <= maxWidth){
            cur.add(words[i]);
            curLength += words[i].length() + 1;
            i++;
        }

        return cur;
    }

    String getCurrentLine(String[] words, int i, List<String> cur, int maxWidth){

        int totalchars = -1;

        for (String s: cur){
            totalchars += s.length() + 1;
        }
        int spaces = maxWidth - totalchars;

          if (i == words.length || cur.size() == 1){
            return String.join(" ",cur) + " ".repeat(spaces);
        }
        int numwords = cur.size()-1;
        int leftspaces = spaces % numwords;
        int equalspaces = spaces/numwords;

        for (int id = 0; id < leftspaces;id ++){
            cur.set(id, cur.get(id) + " ");
        }

        for (int id = 0; id < numwords; id++){
            cur.set(id,cur.get(id) + " ".repeat(equalspaces));
        }

    return String.join(" ", cur);
    }
}