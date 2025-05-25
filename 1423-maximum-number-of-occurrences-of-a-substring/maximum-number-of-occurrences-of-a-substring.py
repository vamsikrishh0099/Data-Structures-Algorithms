class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        left = 0
        result = defaultdict(int)
        freqs = defaultdict(int)
        for right, num in enumerate(s):
            freqs[num] += 1
            while (right - left + 1) >= minSize and (right - left + 1) <= maxSize:
                if len(freqs) <= maxLetters:
                    result[s[left:right + 1]] += 1
                freqs[s[left]] -= 1
                if not freqs[s[left]]:
                    freqs.pop(s[left])
                left += 1
                
        return max(result.values()) if result else 0