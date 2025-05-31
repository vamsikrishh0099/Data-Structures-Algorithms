class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector_map = {}

        for i,num in enumerate(nums):
            self.vector_map[i] = num

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for k,v in self.vector_map.items():
            if k in vec.vector_map:
                ans += v*(vec.vector_map[k])

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


    """
    save the input nums as a hashmap: (index) -> val 
    for dot product, iterate map and multiply. 


    """