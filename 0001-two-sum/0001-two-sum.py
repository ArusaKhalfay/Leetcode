class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff not in d:
                d[nums[i]] = i
            else:
                return [d[diff], i]
        return None
                
        