class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)/2
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for key, value in d.items():
            if value > m:
                return key
        