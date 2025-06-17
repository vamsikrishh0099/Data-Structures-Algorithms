class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        s1, s2, s3 = str(num1), str(num2), str(num3)
        def convert_s(s: str) -> str:
            return "0" * (4 - len(s)) + s
        s1, s2, s3 = convert_s(s1), convert_s(s2), convert_s(s3)
        res = [min(s1[i], s2[i], s3[i]) for i in range(4)]
        return int("".join(res))


