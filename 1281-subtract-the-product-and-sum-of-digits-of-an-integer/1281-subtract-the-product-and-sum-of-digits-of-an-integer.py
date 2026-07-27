class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        y=n
        sm=0
        pro=1
        while y>0:
            r=y%10
            sm+=r
            pro*=r
            y//=10
        return pro-sm