class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}

        for i,c in enumerate(order):
            mp[c] = i

        s_list = list(s)
        s_list.sort(key = lambda x: mp.get(x, len(s)))

        return "".join(s_list)