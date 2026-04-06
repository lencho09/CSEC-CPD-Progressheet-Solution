class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current = sum(nums)
        total = len(nums) / 2 * (1 + len(nums))

        return int(total - current)
