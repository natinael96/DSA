class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        def winner(ply1, ply2, nums, turn):
            if len(nums) == 0:    
                return ply1 >= ply2
            
            if turn == 1:
                choice1 = nums[0]
                choice2 = nums[-1]
                score1 = ply1 + choice1
                score2 = ply1 + choice2
                return (
                    winner(score1,ply2,nums[1:],2) or winner(score2,ply2,nums[:-1],2))
            else:
                choice1 = nums[0]
                choice2 = nums[-1]
                score1 = ply2 + choice1
                score2 = ply2 + choice2
                return (winner(ply1,score1,nums[1:],1) and winner(ply1,score2,nums[:-1],1))
        return winner(0,0,nums,1)
    
