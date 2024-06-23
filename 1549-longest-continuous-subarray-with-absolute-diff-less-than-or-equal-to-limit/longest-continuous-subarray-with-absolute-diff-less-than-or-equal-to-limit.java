
class Solution {
    public int longestSubarray(int[] nums, int limit) {
        int start = 0;
        int end = 0;
        int min = nums[0];
        int max = min;
        int ans = 1;
        Queue<int[]> minheap = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        Queue<int[]> maxheap = new PriorityQueue<>((a,b) -> b[0] - a[0]);

        while (start < nums.length && end < nums.length){
            int ele1 = nums[start];
            int ele2 = nums[end];

            minheap.offer(new int[]{ele2, end});
            maxheap.offer(new int[]{ele2, end});

            while(maxheap.peek()[0] - minheap.peek()[0] > limit){
                 start = Math.min(maxheap.peek()[1], minheap.peek()[1]) + 1;

                while (maxheap.peek()[1] < start){
                    maxheap.poll();
                }

                while (minheap.peek()[1] < start){
                    minheap.poll();
                }
            }
            ans = Math.max(ans, end - start + 1);

            end++;
        }

        return ans;
    }
}
