class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp1 = {}
        for i, num in enumerate(nums):
            findNum = target - num
            if findNum in mp1:
                return [mp1[findNum], i]
            mp1[num] = i
                

        