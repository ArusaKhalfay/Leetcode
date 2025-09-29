class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []

        for i in range(0, len(nums)):
            squared_result = nums[i]*nums[i]
            squares.append(squared_result)
        print(squares)
        squares.sort()
        return squares