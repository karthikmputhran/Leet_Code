class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        mc=max(candies)
        for i in candies:
            if (i+extraCandies)>=mc:
                a.append(True)
            else:
                a.append(False)
        return a