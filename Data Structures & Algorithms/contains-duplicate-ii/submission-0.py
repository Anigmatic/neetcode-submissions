class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        intmap = {}
        for i,num in enumerate(nums):
            if num in intmap and i - intmap[num] <= k:
                return True
            intmap[num] = i
        return False