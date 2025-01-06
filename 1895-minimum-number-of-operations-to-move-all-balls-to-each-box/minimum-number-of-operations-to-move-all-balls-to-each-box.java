class Solution {
    public int[] minOperations(String boxes) {
        
        List<Integer> ones = new ArrayList<>();
        int[] ans = new int[boxes.length()];
        for (int i = 0; i < boxes.length(); i++){
            if (boxes.charAt(i) == '1'){
                ones.add(i);
            }
        }

        for (int i = 0 ; i < boxes.length(); i++){
            for (int pos: ones){
                if (pos != i){
                    ans[i] += Math.abs(i - pos);
                }
            }
        }

        return ans;
    }
}