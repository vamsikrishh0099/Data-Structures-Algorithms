class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        treat each row as sorted list.
        so it is kth smallest element given n sorted lists problem.
        use minheap and do process until kth element.
        """

        pq = []

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            heapq.heappush(pq, (matrix[i][0], i, 0)) # (value, row_number, array_index)
        
        ans = 0
        while k > 0 and pq:
            k -= 1
            val, row_number, array_index = heapq.heappop(pq)
            ans = val
            if array_index < cols - 1:
                heapq.heappush(pq, (matrix[row_number][array_index + 1], row_number, array_index + 1))
        
        return ans


