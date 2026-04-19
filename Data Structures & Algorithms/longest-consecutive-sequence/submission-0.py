class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        num_set = set(nums)

        for num in nums:
            if (num - 1) not in num_set:
                streak = 0
                curr = num
                while curr in num_set:
                    streak += 1
                    curr += 1
                result = max(result, streak)
        return result