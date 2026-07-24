class Solution:
    def defangIPaddr(self, addr: str) -> str:
        ## eturn addr.replace(".","[.]")
        s=[]
        for i in addr:
            if i==".":
                s.append("[.]")
            else:
                s.append(i)
        return "".join(s)