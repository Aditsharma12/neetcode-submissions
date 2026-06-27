class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el]=1
            ans=[]
        for key,value in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            ans.append(key)
        return ans[0:k]
