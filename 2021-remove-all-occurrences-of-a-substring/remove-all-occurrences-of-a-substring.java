class Solution {
    public String removeOccurrences(String s, String part) {
        
        Stack<Character> s1 = new Stack<>();
        Stack<Character> s2 = new Stack<>();
        StringBuilder ans = new StringBuilder();


        int id = 0;

        int charId = part.length()-1;

        while(id < s.length()){
           
               
            if (s.charAt(id) == part.charAt(charId)){
                s2.push(s.charAt(id));
                charId--;

                while(charId >= 0 && !s1.isEmpty() && s1.peek() == part.charAt(charId)){
                    s2.push(s1.pop());
                    charId--;
                }
                if (charId == -1){
                    // ther's a mathc'
                    s2.clear();
                charId = part.length()-1;
                }
                else{
                    while(!s2.isEmpty()) s1.push(s2.pop());
                    charId = part.length()-1;
                }
                 
            }
            else{
                  s1.push(s.charAt(id));
            }
            
          
            id++;
        }

        while (!s1.isEmpty()) ans.append(s1.pop());

        return ans.reverse().toString();


    }
    

}