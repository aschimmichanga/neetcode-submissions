class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)

        for num in nums:
            numFrequencies[num] += 1

        sortedNumFrequencies = sorted(numFrequencies.items(), key=lambda item: item[1])

        topKFrequentNums = []
        while len(topKFrequentNums) < k:
            topKFrequentNums.append(sortedNumFrequencies.pop()[0])
        
        return topKFrequentNums

