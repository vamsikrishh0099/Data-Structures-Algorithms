class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        sorted_list = []
        ans = []
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        
        for key,v in mp.items():
            sorted_list.append((v,key))

        sorted_list.sort(key = lambda x: x[0], reverse = True)

        for i in range(k):
            ans.append(sorted_list[i][1])

        return ans
