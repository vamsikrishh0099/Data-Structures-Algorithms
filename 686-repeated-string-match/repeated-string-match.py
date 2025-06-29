class Solution:
    def repeatedStringMatch2(self, a: str, b: str) -> int:
        """
        1. find all possible starting indices.
        2. if no starting indices -> return -1
        3. for each starting index, find how many times we need to append string. 
            chars needed = len(b) - (num chars from start to end)
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

    # Answer 2:
        # Append a to itself until len(a) >= len(b)
        # check for b in a. if yes, return count.
        # if not, append once more to confirm if b starts from end of a.

    def repeatedStringMatch(self, a: str, b: str) -> int:
        checker = a[:]
        count = 1
        while len(checker) < len(b):
            checker = checker + a[:]
            count += 1

        if b in checker:
            return count

        checker += a
        if b in checker:
            return count + 1

        return -1

