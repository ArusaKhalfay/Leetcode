class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for x in range(0, len(nums)+1):
            count = 0
            for i in range(0, len(nums)):
                if nums[i] >= x:
                    count += 1
                
            if x == count:
                return x
                break
        
        return -1
            
        