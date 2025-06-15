class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        1. counter 
        2. put in a list like - (freq, char) and sort in desc
        3. prepare ans list
        4. greedily place characters starting with max freq character.
        5. while placing, check if its adjacent are same or not
        6. if same, return "" 
        7. if not, place it and go ahead.


        """
        max_heap = []
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1

        for k,v in mp.items():
            max_heap.append((-v, k))

        heapq.heapify(max_heap)

        ans = []

        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            ans = ans + [char1, char2]

            freq1 += 1
            freq2 += 1

            if freq1 < 0:
                heapq.heappush(max_heap, (freq1, char1))
            
            if freq2 < 0:
                heapq.heappush(max_heap, (freq2, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)

            if freq < -1:
                return ""
            ans.append(char)

        return "".join(ans)