class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumi=0
        for i in range(0,len(nums)+1):
            sumi+=i
        ok=sum(nums)
        if sumi-ok == 0:
            return 0
        else:
            return sumi-ok