class Solution:
    def kthCharacter(self, k: int) -> str:
        

        def operate(word):
            size = len(word)

            for i in range(size):
                new_char = "a" if word[i] == "z" else chr(ord(word[i]) + 1)
                word.append(new_char)


        word = ["a"]

        while len(word) < k:
            operate(word)

        
        return word[k-1]

