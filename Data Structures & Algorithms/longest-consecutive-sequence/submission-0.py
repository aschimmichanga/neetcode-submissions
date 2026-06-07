class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen_nums = set()
        for num in nums:
            seen_nums.add(num)

        longest_length = 0
        for num in nums:
            if not num - 1 in seen_nums:
                counter = 0
                while num + counter in seen_nums:
                    counter += 1
                longest_length = max(longest_length, counter)
        return longest_length
