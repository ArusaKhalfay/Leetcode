class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_array = list(range(0, len(nums)+1))

        return sum(new_array) - sum(nums)
        