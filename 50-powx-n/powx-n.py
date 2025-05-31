class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return self.binaryexp(x,n)
    
    def binaryexp(self, x, n):

        if n == 0:
            return 1.0

        if n < 0:

            return 1/(self.binaryexp(x, -n))

        if n%2 == 0:
            return self.binaryexp(x*x, n/2)
        else:
            return x*self.binaryexp(x*x, (n-1)/2)