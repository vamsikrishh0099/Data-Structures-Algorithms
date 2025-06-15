class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}
        ans = []

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in mp:
                mp[sorted_str].append(s)
            else:
                mp[sorted_str] = [s]

        for k,v in mp.items():
            ans.append(v)
        return ans
