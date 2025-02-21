class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                increasing = False
                break
        
        if increasing:
            return True

        decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
                break
        
        return decreasing




        
