class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=list(s)
        seen = set()
        left=0
        right=0
        maxlen=0
        while(right<len(arr)):
            if(arr[right] not in seen):
                seen.add(arr[right])
                right+=1
            else:
                seen.remove(arr[left])
                left+=1
            maxlen=max(right-left,maxlen)
        return maxlen