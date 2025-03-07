class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1 = {}

        for i in range(0, len(nums1)):
            if nums1[i] in d1:
                d1[nums1[i]] += 1
            else:
                d1[nums1[i]] = 1

        for num in nums2:
            if num in d1 and d1[num] > 0:
                res.append(num)
                d1[num] -= 1
        
        return res