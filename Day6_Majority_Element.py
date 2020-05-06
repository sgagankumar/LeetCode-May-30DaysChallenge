class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        for num in set(nums):
            if nums.count(num) > length//2:
                return num