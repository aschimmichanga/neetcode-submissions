class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for firstIndex, firstNum in enumerate(nums):
            for secondIndex, secondNum in enumerate(nums):
                if firstIndex != secondIndex and (firstNum + secondNum) == target:
                    return [firstIndex, secondIndex]
        return [0, 0]