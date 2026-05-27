class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = set()
        for num in nums:
            hashLength = len(numHash)
            numHash.add(num)
            if len(numHash) == hashLength:
                return True
        return False