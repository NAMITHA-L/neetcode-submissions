class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            a = tuple(sorted(i))
            if a not in d:
                d[a] = []
            d[a].append(i)
        l = []
        for i in d.values():
            l.append(i)
        return l