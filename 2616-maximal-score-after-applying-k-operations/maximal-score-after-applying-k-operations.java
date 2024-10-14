class Solution {
    public long maxKelements(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int num: nums){
            pq.offer(num);
        }

        long ans = 0; 

        while (k > 0){
            int num = pq.peek();
            ans += num;
            pq.poll();
            pq.offer(Math.ceilDiv(num, 3));
            k--;
        }

        return ans;

    }
}