class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        """
        This is not the best solution at all. 
        Not ideal for 0/1 knapsack as it is a overkill. 
        sorting and picking top k elements is better approach. 
        """
        n = len(nums)
        # Memoization table: dp[index][count] = (max_sum, subsequence)
        dp = {}
        
        def knapsack(index: int, count: int) -> tuple[int, List[int]]:
            # Base cases
            if count == k:
                return 0, []
            if index >= n or n - index < k - count:  # Not enough elements left
                return float('-inf'), []
            if (index, count) in dp:
                return dp[(index, count)]
            
            # Include current element
            inc_sum, inc_seq = knapsack(index + 1, count + 1)
            inc_sum += nums[index]
            inc_seq = [nums[index]] + inc_seq
            
            # Exclude current element
            exc_sum, exc_seq = knapsack(index + 1, count)
            
            # Choose the option with the maximum sum
            if inc_sum > exc_sum:
                dp[(index, count)] = (inc_sum, inc_seq)
            else:
                dp[(index, count)] = (exc_sum, exc_seq)
                
            return dp[(index, count)]
        
        # Start from index 0 with count 0
        return knapsack(0, 0)[1]

        