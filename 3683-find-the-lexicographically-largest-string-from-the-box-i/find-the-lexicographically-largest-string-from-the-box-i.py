class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        find the length of the answer first.
        1. make all other words as small as possible. 
        2. size - (num_friends - 1) Ex: 4 - 1 = 3, 4 - 3 = 1
        3. once we have size of answer, append all possible answers to a list. sort desc and take first. 
        """

        if numFriends == 1:
            return word
        n = len(word)
        ans_size = n - (numFriends - 1)

        max_char = word[0]
        for c in word:
            if c > max_char:
                max_char = c
        all_ans = []

        best = ""
        for i in range(n):
            if word[i] == max_char:
                if best < word[i:i+ans_size]:
                    best = word[i:i+ans_size]
                
        
        return best



