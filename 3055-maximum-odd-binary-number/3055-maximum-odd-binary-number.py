class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0

        for i in range(0, len(s)):
            if s[i] == "1": # beaware of strings
                count += 1
            else:
                continue

        return (count - 1) * "1" + (len(s) - count) * "0" + "1"