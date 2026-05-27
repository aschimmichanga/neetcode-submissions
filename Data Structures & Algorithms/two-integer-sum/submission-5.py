class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = []
        for index, num in enumerate(nums):
            sortedNums.append([num, index])

        sortedNums.sort()

        index1, index2 = 0, len(nums) - 1

        while index1 < index2:
            currentSum = sortedNums[index1][0] + sortedNums[index2][0]
            if currentSum == target:
                result = [sortedNums[index1][1], sortedNums[index2][1]]
                result.sort()
                return result
            elif currentSum < target:
                index1 += 1
            else:
                index2 -= 1

        return [-1, -1]