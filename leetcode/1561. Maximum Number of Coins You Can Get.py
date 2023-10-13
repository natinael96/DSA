class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # piles.sort()
        # return sum(itertools.islice(piles, len(piles)//3, len(piles), 2))
        piles.sort()
    
        n = len(piles) // 3  # Number of iterations 
        your_coins = 0
        
        for i in range(n, len(piles), 2):
            your_coins += piles[i]
        
        return your_coins
