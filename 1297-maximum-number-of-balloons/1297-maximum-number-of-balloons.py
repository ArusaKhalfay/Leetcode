class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for i in range(0, len(text)):
            if text[i] in d:
                d[text[i]] += 1
            else:
                d[text[i]] = 1

        balloonmap = {}
        s = "balloon"
        for j in range(0, len(s)):
            if s[j] in balloonmap:
                balloonmap[s[j]] += 1
            else:
                balloonmap[s[j]] = 1

        res = len(text)
        for c in balloonmap:
            if c in d:
                res = min(res, d[c]//balloonmap[c])
            else:
                return 0
        return res
