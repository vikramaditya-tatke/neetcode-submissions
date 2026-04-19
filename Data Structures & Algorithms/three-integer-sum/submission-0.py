class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                three_sum = sorted_nums[left] + sorted_nums[right] + num
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([num, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

        return result