class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        Queue<int[]> maxHeap = new PriorityQueue<>((a,b) -> b[0] - a[0]);
        int[] ans = new int[nums.length - k + 1+1];
        int ind = 0;
        int start = 0;
int[] result = new int[nums.length - k + 1]; // This will hold the maximums for each window
        int ri = 0; // Index for result array

        // Initialize the max heap with the first 'k' elements
        for (int i = 0; i < k; i++) {
            maxHeap.add(new int[]{nums[i], i});
        }

        // Store the maximum for the first window
        result[ri++] = maxHeap.peek()[0];

        for (int i = k; i < nums.length; i++) {
            // Add new element from the window into the max heap
            maxHeap.add(new int[]{nums[i], i});
            
            // Remove the elements not within the window (lazy removal)
            while (maxHeap.peek()[1] <= i - k) {
                maxHeap.poll();
            }

            // The current max will always be the root of the max heap
            result[ri++] = maxHeap.peek()[0];
        }

        return result;

    }
}