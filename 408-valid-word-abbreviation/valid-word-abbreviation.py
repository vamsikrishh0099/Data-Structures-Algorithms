class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0,0
        m,n = len(word), len(abbr)

        while i < m and j < n:

            if word[i] == abbr[j]:
                i += 1
                j += 1

            elif abbr[j] == "0":
                return False
            
            elif abbr[j].isnumeric():

                k = j 

                while k < n and abbr[k].isnumeric():
                    k += 1

                num = int(abbr[j:k])
                i += num
                j = k
            else:
                return False

        return i == m and j == n