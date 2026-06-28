import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = 1
        ans = []

        for li in nums:
            pr *= li

        for li in nums:
            if li == 0:
                temp = nums.copy()
                temp.remove(0)
                ans.append(math.prod(temp))
            else:
                ans.append(pr // li)

        return ans