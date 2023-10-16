class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = len(skill)//2
        team_arr = [0]*teams
        team_arr[0]  = skill[0] + skill[len(skill) - 1]
        left, right = 1, len(skill) - 2
        chem = skill[0] * skill[len(skill) - 1]
        while left <= right:
            team_arr[left] = skill[left] + skill[right]
            if team_arr[left] == team_arr[left-1]:
                chem += skill[left] * skill[right]
                left+=1
                right-=1
            else:
                return -1
        
        return chem
            