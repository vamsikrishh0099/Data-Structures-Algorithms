class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        words = sentence.split(" ")
        vowels = {'a', 'e', 'i', 'o','u'}

        suffix_length = 1

        for i, word in enumerate(words):
            if word[0].lower() in vowels:
                ans.append(word + "ma" + "a"*suffix_length)

            else:
                ans.append(word[1:] + word[0] + "ma" + "a"*suffix_length)

            suffix_length += 1

        return " ".join(ans)
