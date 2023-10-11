class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        return s_list == t_list
    