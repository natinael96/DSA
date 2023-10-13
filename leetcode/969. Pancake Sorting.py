class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip = []
        if arr == sorted(arr):
            return flip
        for i in range(len(arr),0,-1):
            cur_max = max(arr[:i]) 
            max_idx = arr.index(cur_max)
            if max_idx == i - 1:
                continue
            if max_idx != 0:
                arr[:max_idx+1]= arr[:max_idx+1][::-1]
                flip.append(max_idx+1) 
            arr[:i] = arr[:i][::-1]
            flip.append(i)
        return flip
    