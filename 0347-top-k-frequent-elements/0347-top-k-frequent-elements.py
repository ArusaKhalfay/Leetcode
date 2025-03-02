class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        sorted_values = sorted(d.items(), key= lambda x:x[1], reverse = True)
        print(sorted_values)
        res = []

        i = 0
        while k > i:
            res.append(sorted_values[i][0])
            i += 1

        return res
