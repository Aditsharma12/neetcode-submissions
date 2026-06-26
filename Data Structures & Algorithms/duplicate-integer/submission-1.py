class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        d=False
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num]=1
        return False