class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sub = 0
        intmap = {}
        for i,num in enumerate(nums):
            if num in intmap:
                if i - intmap[num] <= k:
                    return True
            intmap[num] = i
        return False