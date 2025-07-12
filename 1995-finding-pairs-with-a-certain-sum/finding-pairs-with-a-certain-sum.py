class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums2_map = {}
        self.imap = {}

        self.nums1 = nums1
        self.nums2 = nums2

        for i,num in enumerate(nums2):
            self.nums2_map[num] = self.nums2_map.get(num, set())
            self.nums2_map[num].add(i)
            self.imap[i] = num

    def add(self, index: int, val: int) -> None:
        
        curnum = self.imap[index]
        self.nums2_map[curnum].remove(index)
        self.imap[index] = curnum + val
        
        if self.imap[index] not in self.nums2_map:
            self.nums2_map[self.imap[index]] = set()
        self.nums2_map[self.imap[index]].add(index)



    def count(self, tot: int) -> int:
        ans = 0
        for i, val in enumerate(self.nums1):
            if tot - val in self.nums2_map:
                ans += len(self.nums2_map[tot - val])

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)