class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        1. Find missing before start
        2. do Binary search:
            For each mid, check mid - start.
            Find how many numbers are missing between mid and start  = missed
            if start + missed > k, go left. else go right

        """

        
        n = len(arr)
        # If kth missing is before the first element
        if k <= arr[0] - 1:
            return k

        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            # Count of missing numbers until arr[mid]
            missing = arr[mid] - (mid + 1)
            if missing < k:
                start = mid + 1
            else:
                end = mid - 1
        
        # After binary search, kth missing number is between arr[end] and arr[start]
        return start + k


            