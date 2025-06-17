class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}

        for c in s:
            mp[c] = mp.get(c, 0) + 1

        a = [(freq, char) for char, freq in mp.items()]
        a.sort(key = lambda x: (x[0], x[1]), reverse = True)

        ans = [char*freq for freq, char in a]

        return "".join(ans)