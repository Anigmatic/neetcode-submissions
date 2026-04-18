class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = maxnum = 0
        for num in nums:
            count[num] += 1
            if maxnum < count[num]:
                result = num
                maxnum += count[num]
        return result

