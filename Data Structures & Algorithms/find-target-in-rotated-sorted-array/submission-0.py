class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]==target:
                k=i
                break
            else:
                k=-1
        return k
