class Solution:
    def isPalindrome(self, s: str) -> bool:
        li=[]
        s=s.upper()
        for i in s:
            if i.isalnum():
                li.append(i)
        return li==li[::-1]