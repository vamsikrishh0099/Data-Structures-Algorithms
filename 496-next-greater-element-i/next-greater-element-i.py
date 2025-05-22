class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        ans = []
        nge = [-1]*len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            while st and num >= st[-1]:
                st.pop()

            if st:
                nge[i] = st[-1]

            st.append(num)

        mp = {}
        for num in nums1:
            mp[num] = -1

        for i,num in enumerate(nums2):
            if num in mp:
                mp[num] = i

        for k,v in mp.items():
            if mp[k] != -1:
                ans.append(nge[mp[k]])
            else:
                ans.append(-1)

        return ans
