class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {}
        d2 = {}

        for i in range(0, len(words1)):
            if words1[i] in d1:
                d1[words1[i]] += 1
            else:
                d1[words1[i]] = 1

        for i in range(0, len(words2)):
            if words2[i] in d2:
                d2[words2[i]] += 1
            else:
                d2[words2[i]] = 1
        
        count = 0
        for word in d1:
            if d1[word] == 1 and word in d2 and d2[word] == 1:
                count += 1
        
        return count