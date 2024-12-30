class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            elif nums[i] not in d:
                d[nums[i]] = 1
        
        for key, value in d.items():
            if value > 1:
                return True
        
        return False
            
        
        