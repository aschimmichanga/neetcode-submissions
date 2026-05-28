class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = defaultdict(int)

        for num in nums:
            numFrequencies[num] += 1

        sortedNumFrequencies = sorted(numFrequencies.items(), key=lambda item: item[1], reverse=True)

        currentRank = 1
        currentRankFreq = sortedNumFrequencies[0][1]

        topKFrequentNums = []

        for num, frequency in sortedNumFrequencies:
            if currentRankFreq != frequency:
                # need to update current rank for this num
                currentRank += 1
                currentRankFreq = frequency 

            if len(topKFrequentNums) == k:
                return topKFrequentNums
            
            topKFrequentNums.append(num)    
        
        return topKFrequentNums

