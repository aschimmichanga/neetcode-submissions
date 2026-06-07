class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def calculatePrefixes(prefix_nums: List[int]):
            prefixes = []
            for i in range(len(prefix_nums)):
                if i == 0:
                    prefixes.append(1)
                else:
                    prefixes.append(prefixes[i - 1] * prefix_nums[i-1])
            return prefixes

        prefixes = calculatePrefixes(nums)
        postfixes = calculatePrefixes(nums[::-1])[::-1]
        output = []
        for i in range(len(nums)):
            output.append(prefixes[i] * postfixes[i])
        return output

        # multiply prefixes and postfixes to get results for each num
