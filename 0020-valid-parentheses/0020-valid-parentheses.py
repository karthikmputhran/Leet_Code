class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        K=[]
        for i in range (len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                K.append(s[i])
            else:
                if not K:
                    return False
                top = K.pop()
                if s[i]==')' and top!='(':
                    return False
                if s[i]==']' and top!='[':
                    return False
                if s[i]=='}' and top!='{':
                    return False
        return len(K)==0