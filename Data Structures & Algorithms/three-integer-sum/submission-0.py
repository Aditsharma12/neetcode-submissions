class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third in seen:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    ans.add(triplet)

                seen.add(nums[j])

        return [list(t) for t in ans]