class Solution:
    def reverse(self, x: int) -> int:
        range=(2**31)
        stor=self.palindrome(x)
        if stor < -1*range or stor > range-1:
            return 0
        else:
            return stor
        
    def palindrome(self,n: int) -> int:
        if n==0:
            return 0
        if n>0:
            rev=0
            while n:
                R=n%10
                n=n//10
                rev=rev*10+R
        if n<0:
            n=-1*n
            rev=0
            while n:
                R=n%10
                n=n//10
                rev=rev*10+R
            rev=rev*-1
        return rev


