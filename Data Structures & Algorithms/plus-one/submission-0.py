class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no=0
        an=[]
        for i in digits:
            no=no*10+i
        no+=1
        while no:
            R=no%10
            no=no//10
            an.append(R)
        an.reverse()
        return an
        