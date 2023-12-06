class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictNum = defaultdict(int)
        for i in nums:
            dictNum[i] += 1
        
        dictNum = dict(sorted(dictNum.items(), key=lambda x: x[1], reverse=True))
        out = list(dictNum.keys())[:k]
        
        return out