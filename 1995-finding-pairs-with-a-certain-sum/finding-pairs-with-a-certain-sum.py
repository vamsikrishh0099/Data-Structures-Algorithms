class FindSumPairs:
    """
    if you need to return indices, the map should be: num -> list of indices
    if just count, the map can be: num -> counts (freq counter)
    """
    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums2_map = {}
        self.imap = {}

        self.nums1 = nums1
        self.nums2 = nums2

        for i,num in enumerate(nums2):
            self.nums2_map[num] = self.nums2_map.get(num, 0) + 1
            self.imap[i] = num

    def add(self, index: int, val: int) -> None:
        
        curnum = self.imap[index]
        self.nums2_map[curnum] -= 1
        self.imap[index] = curnum + val
        
        if self.imap[index] not in self.nums2_map:
            self.nums2_map[self.imap[index]] = 0
        self.nums2_map[self.imap[index]] += 1



    def count(self, tot: int) -> int:
        ans = 0
        for i, val in enumerate(self.nums1):
            if tot - val in self.nums2_map:
                ans += self.nums2_map[tot - val]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)