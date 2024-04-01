class Solution {
    public int hIndex(int[] citations) {
        
        Map<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i < citations.length;i++){

            int k = citations[i];
            while(k > 0){
                mp.put(k, mp.getOrDefault(k,0) + 1);
                k--;
            }
        }

        int i = citations.length;
        while (i > 0){
            if (mp.containsKey(i) && mp.get(i) >= i) return i;
            i--;
        }

        return 0;

    }
}