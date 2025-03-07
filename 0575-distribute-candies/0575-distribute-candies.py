class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_candy_types = len(set(candyType))
        n = len(candyType)//2

        return min(n, num_candy_types)