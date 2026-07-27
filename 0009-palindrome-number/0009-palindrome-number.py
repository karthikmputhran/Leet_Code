class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        rev=0
        while y>0:
            r=y%10
            y//=10
            rev=rev*10+r
        return rev==x