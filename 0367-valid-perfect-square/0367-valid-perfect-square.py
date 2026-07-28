class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        y=sqrt(num)//1
        x=sqrt(num)
        if x-y==0:
            return True
        return False