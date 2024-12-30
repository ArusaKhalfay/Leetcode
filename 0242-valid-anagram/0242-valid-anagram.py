class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        for i in range(0, len(s)):
            if s[i] in s1:
                s1[s[i]] += 1
            elif s[i] not in s1:
                s1[s[i]] = 1
        
        for j in range(0, len(t)):
            if t[j] in t1:
                t1[t[j]] += 1
            else:
                t1[t[j]] = 1

        if s1 == t1:
            return True
        else:
            return False


        