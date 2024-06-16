class Solution {
    // public int maxProfit(int[] prices) {
    //     int small = prices[0];
    //     int profit = 0;
    //     for (int i = 1;i<prices.length;i++){
    //         if (prices[i] > small){
    //             profit = Math.max(profit,prices[i] - small);
    //         }
    //         else{
    //             small = prices[i];
    //         }
    //     }

    //     return profit;
    // }

        public int maxProfit(int[] prices) {
            int smallest = prices[0];
            int ans = 0;
            for (int i = 1; i < prices.length;i++){
                if (smallest > prices[i]){
                    smallest = prices[i];
                    continue;
                }
                ans = Math.max(ans, prices[i] - smallest);
            }

            return ans;

    }
}