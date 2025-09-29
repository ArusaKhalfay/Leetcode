class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        res = []

        for i in range(0, len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        print(d)
        sorted_d = sorted(d.items(), key = lambda item: (item[1], -item[0]))

        print(sorted_d)

        for num,freq in sorted_d:
            res.extend([num]*freq)
        
        return res
