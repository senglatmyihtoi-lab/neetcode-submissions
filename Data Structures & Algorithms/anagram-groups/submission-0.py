class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            l[sort].append(i)
        return list(l.values())