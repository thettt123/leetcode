class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        ans = (x2-x1)*(y3-y2) != (x3-x2)*(y2-y1)
        return ans