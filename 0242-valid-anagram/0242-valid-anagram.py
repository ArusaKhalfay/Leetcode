class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for letter in s:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1

        for l in t:
            if l in d2:
                d2[l] += 1
            else:
                d2[l] = 1
        print(d1)
        print(d2)
        if d1 == d2:
            return True
        else:
            return False