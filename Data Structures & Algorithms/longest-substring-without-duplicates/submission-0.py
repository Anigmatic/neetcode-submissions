class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        result = 0
        l = 0
        for i in range(len(s)):
            while s[i] in subset:
                subset.remove(s[l])
                l += 1
            subset.add(s[i])
            result = max(result,i-l+1)
        return result 