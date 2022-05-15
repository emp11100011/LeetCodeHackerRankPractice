class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)




s = Solution()
s.containsDuplicate([1, 2, 2])