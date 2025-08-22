class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []

        start = 0
        cur = 0

        while start < len(chars):
            counter = 0
            for i in range(start, len(chars)):
                if chars[i] == chars[start]:
                    counter += 1
                else:
                    break 
            ans.append(chars[start])
            if counter > 1: 
                ans.extend(list(str(counter)))
            start = start + counter

        for i,val in enumerate(ans):
            chars[i] = val
        return len(ans)