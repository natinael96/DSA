class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = 0 # player
        j = 0 # trainers
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j+=1
        return count
    
soln = Solution()
players = [1,1,1]
trainer =[10]
a = soln.matchPlayersAndTrainers(players, trainer)
print(a)