class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)

        for num in nums:
            numFrequencies[num] += 1

        freqGroupings = [[] for i in range(len(nums) + 1)]

        for num, freq in numFrequencies.items():
            freqGroupings[freq].append(num)

        topKFrequentNums = []
        currFreqNums = freqGroupings.pop()
        while len(topKFrequentNums) < k:
            if not currFreqNums:
                currFreqNums = freqGroupings.pop()
            else:
                topKFrequentNums.append(currFreqNums.pop())
               
        return topKFrequentNums

