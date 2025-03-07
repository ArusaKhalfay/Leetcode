class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            
        max_value = 0
        max_key = 0
        for key, value in d.items():
            if max_value < value:
                max_value = value 
                max_key = key

        return max_key