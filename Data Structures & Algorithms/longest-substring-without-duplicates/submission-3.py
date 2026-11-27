class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        h = {}
        l = 0
        best = 0

        for r, i in enumerate(s):
            if i in h and h[i]>= l:
                l = h[i]+1
            h[i] = r
            best = max(best, r-l+1)
        return best
                