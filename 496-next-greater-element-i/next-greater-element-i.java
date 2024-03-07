class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        

        Stack<Integer> st = new Stack<>();
        int[] nge = new int[nums2.length];

        Map<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i< nums2.length;i++){
            mp.put(nums2[i], i);
        }


        for (int i = nums2.length-1; i>=0;i--){
            
            while(!st.isEmpty() && nums2[i] > st.peek()){
                st.pop();
            }
            if (st.isEmpty()) nge[i] = -1;
            else nge[i] = st.peek();

            st.push(nums2[i]);
        }

        int[] ans = new int[nums1.length];

        for (int i = 0; i< nums1.length;i++){
            int cur = nums1[i];
            ans[i] = nge[mp.get(cur)];

        }

        return ans;
        
    }
}
