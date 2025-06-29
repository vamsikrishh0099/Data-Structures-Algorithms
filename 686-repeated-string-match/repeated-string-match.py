class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        1. find all possible starting indices.
        2. if no starting indices -> return -1
        3. for each starting index, find how many times we need to append string. 
            chars needed = len(b) - len(a) - i - 1
            num times to append = chars needed//len(a) + 1
            append that many times and check. 
        """

        def append_string(a, start):
            chars_needed = len(b) - (len(a) - start)
            times = math.ceil(chars_needed/len(a))

            s = [a]
            for t in range(times):
                s.append(a)
            
            return "".join(s), times + 1

        starting_indices = [ind for ind,c in enumerate(a) if b[0] == c]

        if not starting_indices:
            return -1
        
        for start in starting_indices:
            appended_string, times = append_string(a, start)
            if appended_string[start: start + len(b)] == b:
                return times
        
        return -1

