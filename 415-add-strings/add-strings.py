class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        ans = []
        carry = 0 
        
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            value = (n1 + n2 + carry)%10
            carry = (n1 + n2 + carry)//10

            ans.append(str(value))
            i -= 1
            j -= 1

        if carry > 0:
            ans.append(str(carry))
            
            
        t = [n for n in ans[::-1]]
        return ''.join(t)
            



            

