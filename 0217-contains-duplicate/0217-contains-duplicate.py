class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x=len(nums)
        for i in range(1,x):
            if nums[i]==nums[i-1]:
                return True
        return False