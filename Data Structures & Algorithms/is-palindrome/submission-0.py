class Solution:
    def isPalindrome(self, s: str) -> bool:
        li=list(s.upper())
        li2=[x for x in li if x!=" "]
        li2=[x for x in li if x.isalnum()]
        return li2==li2[::-1]
        