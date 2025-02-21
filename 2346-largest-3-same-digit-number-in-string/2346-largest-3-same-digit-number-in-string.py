class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        val = float(-inf)

        for i in range(0, len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                tmp = num[i:i+3]
                if val <= int(tmp):
                    val = int(tmp)
                    res = tmp
        
        return res
