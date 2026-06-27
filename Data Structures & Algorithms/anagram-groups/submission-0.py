class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for str in strs:
            key = "".join(sorted(str))
            if key not in grps:
                grps[key]=[]
            grps[key].append(str)
        return list(grps.values())
        