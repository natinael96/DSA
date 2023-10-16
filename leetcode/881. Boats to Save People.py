class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lft , rgt = 0, len(people)-1
        count = 0
        while lft <= rgt:
            if people[lft] + people[rgt] <= limit:
                lft += 1
            rgt -= 1
            count+=1
        return count

    