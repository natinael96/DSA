class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        lencand = len(candidates)
        out = []

        def backtrack(current_combo, current_sum, index):
            if current_sum == target:
                out.append(current_combo[:])
            if current_sum > target or index >= lencand:
                return
            for i in range(index, lencand):
                candidate = candidates[i]
                current_combo.append(candidate)
                backtrack(current_combo, current_sum + candidate, i)
                current_combo.pop()
        candidates.sort()
        backtrack([],0,0)
        return out

