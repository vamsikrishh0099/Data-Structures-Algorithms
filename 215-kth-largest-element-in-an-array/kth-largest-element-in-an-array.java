class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int x: nums){
            pq.add(x);
        }

    for (int i = 0; i <k-1;i++){
        pq.poll();
    }

        return pq.peek();
        
    }
}