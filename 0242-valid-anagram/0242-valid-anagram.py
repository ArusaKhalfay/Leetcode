class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in range(0, len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
        
        for j in range(0, len(t)):
            if t[j] in d2:
                d2[t[j]] += 1
            else:
                d2[t[j]] = 1
        
        if d1 == d2:
            return True
        else:
            return False
        