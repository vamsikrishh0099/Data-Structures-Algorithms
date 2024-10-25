class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        

        int start = 0;
        int end = 0;

        int min_size = Integer.MAX_VALUE;
        int running_sum = 0;

        while (end < nums.length){
            running_sum += nums[end];

            if (running_sum >= target){


                while(running_sum >= target && start <= end ){
                    running_sum -= nums[start];
                    start++;
                }
            min_size = Math.min(min_size, end - start + 2);
            }

            end++;
          
        }

        return min_size==Integer.MAX_VALUE?0:min_size;
    }
}