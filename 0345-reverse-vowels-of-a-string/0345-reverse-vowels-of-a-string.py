class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        right=len(s)-1
        left=0
        v=set("AEIOUaeiou")
        while left<right:
            if s[left]in v and s[right] in v:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left] not in v :
                left+=1
            elif s[right] not in v:
                right-=1
        return ''.join(s)