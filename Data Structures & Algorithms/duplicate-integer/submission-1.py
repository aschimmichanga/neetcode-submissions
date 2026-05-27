class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = set()
        for num in nums:
            if num in numHash:
                return True
            numHash.add(num)
        return False