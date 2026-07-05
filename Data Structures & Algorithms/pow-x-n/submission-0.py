class Solution:
    def myPow(self, x: float, n: int) -> float:
        pr=1.00000
        if n>0:
            while n:
                pr*=x
                n=n-1
        if n<0:
            n=-1*n
            while n:
                pr/=x
                n=n-1
        return pr
            
        