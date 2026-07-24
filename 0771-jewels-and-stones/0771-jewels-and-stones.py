class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        j=set(jewels)
        for stone in stones:
            if stone in jewels:
                count+=1
        return count