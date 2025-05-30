class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        

    # """
    # s = yyyzz
    # k = 1

    # mp: 
    # y --> 3
    # z --> 2

    # freq_arr of size max(freq) each index has list of chars 

    # start counting from left (least freq) and count how many chars are removed. do it until we reach k. 

    # """
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        size = len(counter)
        if size <= k:
            return 0

        max_freq = max(counter.values())

        freq_arr =[ [] for _ in range(max_freq + 1) ]

        for c, freq in counter.items():
            freq_arr[freq].append(c)
        ans = 0
        for i in range(len(freq_arr)):
            freq = i
            chars_list = freq_arr[i]
            for c in chars_list:
                
                chars_to_remove = size - k 
                if chars_to_remove > 1:
                    ans += freq
                    size = size - 1
                    continue
                
                ans += freq
                return ans

        return ans 

        




    






