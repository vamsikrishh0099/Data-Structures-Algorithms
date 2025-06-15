# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:

        celeb = 0

        for i in range(1, n):
            if knows(celeb, i):
                celeb = i
        

        if self.is_celeb(celeb, n):
            return celeb
        
        return -1
    
    def is_celeb(self, celeb, n):

        for i in range(n):
            if i != celeb:
                if knows(celeb, i) or not knows(i, celeb):
                    return False

        return True
        