class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_c = Counter(s) 
        counter_t = Counter(t)

        return counter_c == counter_t