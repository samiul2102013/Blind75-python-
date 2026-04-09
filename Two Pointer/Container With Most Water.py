from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            j,k = i , len(heights) - 1
            weight = k - j
             
            while j < k:
                hight = 5000
                hight = min(heights[j], heights[k])
                cur_water = weight * hight
                k -= 1
                max_water = max(max_water, cur_water)

        return max_water



sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])