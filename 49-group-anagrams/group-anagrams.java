class Solution {
//     public List<List<String>> groupAnagrams(String[] strs) {
//         Map<String,List<String>> mp = new HashMap<>();

//         List<List<String>> ans = new ArrayList<>();

//         for (String s:strs){
//             char[] cc = s.toCharArray();
//             Arrays.sort(cc);
//             String s2  = new String(cc);

//             if (mp.containsKey(s2)){
//                 mp.get(s2).add(s);

//             }
//             else{
//                 List<String> sub = new ArrayList<>();
//                 sub.add(s);
//                 mp.put(s2,sub);
//             }
//         }

//         for (Map.Entry<String,List<String>> etr: mp.entrySet()){
//             ans.add(etr.getValue());
//         }

// return ans;


//     }

 public List<List<String>> groupAnagrams(String[] strs) {
     List<List<String>> ans = new ArrayList<>();
     Map<String, List<String>> mp = new HashMap<>();

     int[] counts = new int[26];

     for (String s: strs){
         Arrays.fill(counts,0);

         for (char c: s.toCharArray()){
             counts[c - 'a']++;
         }

         StringBuilder tempS = new StringBuilder();
         tempS.append("#");
         for (int c: counts){
             tempS.append(c);
             tempS.append("#");
         }
         String curString = tempS.toString();

         if (!mp.containsKey(curString)){
             mp.put(curString, new ArrayList<String>());

         }
         mp.get(curString).add(s);



     }

     for (Map.Entry<String,List<String>> etr: mp.entrySet()){
         ans.add(etr.getValue());
     }

     return ans;

      }
}