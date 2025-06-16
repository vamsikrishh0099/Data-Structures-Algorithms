class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        sort both in descending order
        sort nums 2 with having original index too 

        now iterate nums2. 
        if we can use current element from nums1, then assign it to original index of ans, and increment
        index of sorted nums1.
        if not, simply leave it and try to check for next element of nums2
        """

        sorteda = sorted(nums1, reverse = True)
        sortedb = sorted(enumerate(nums2), key=lambda x: (x[1], x[0]), reverse=True)  # descending order with original index


        ans = [-1]*len(nums2)

        a_ind = 0

        for i, (org_ind, target) in enumerate(sortedb):
            if sorteda[a_ind] > target:
                ans[org_ind] = sorteda[a_ind]
                a_ind += 1

        
        for i in range(len(nums2)):
            if ans[i] == -1:
                ans[i] = sorteda[a_ind]
                a_ind += 1
        return ans

        