class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        original_money = money
        for i in range(0, 2):
            money -= prices[i]
        
        if money >= 0:
            return money
        else:
            return original_money

