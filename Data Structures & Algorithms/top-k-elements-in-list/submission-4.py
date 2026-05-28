class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)

        for num in nums:
            numFrequencies[num] += 1

        heap = []
        for num in numFrequencies.keys():
            heapq.heappush(heap, (numFrequencies[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        topKFrequentNums = []
        for i in range(k):
            topKFrequentNums.append(heapq.heappop(heap)[1])
               
        return topKFrequentNums

