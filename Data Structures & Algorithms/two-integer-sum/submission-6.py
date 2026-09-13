class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## using a hash map
        ## store values with indices
        # each time we iterate through the array at a number
        # we check if there is a value in our map that
        # adds up to create the target
        # return the indices with the smaller index first
        mp = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mp:
                return [mp[diff], i]
            mp[num] = i
            



        