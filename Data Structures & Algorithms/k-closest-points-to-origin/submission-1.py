class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            dist = x*x + y*y
            distances.append((dist, [x, y]))

            distances.sort()

        return [point for _, point in distances[:k]]
        


        