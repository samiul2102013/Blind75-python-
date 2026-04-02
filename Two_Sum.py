class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}

        for i,n in enumerate(nums):
            targeted_value = target - n
            if targeted_value in hm:
                return [hm[targeted_value], i]
            hm[n] = i
            
    
sol = Solution()
sol.nums = [2,7,11,15]
sol.target = 9
li = []
li =sol.twoSum(sol.nums, sol.target)

print(li)