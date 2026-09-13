class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # hash map
       ## as we do one pass
       ## we go through and add each number to a hashmap {indices, number}
       ## every time we stop at a number, look for a number in the hashmap
       ## and see if the sum adds up to our target number
       ## if so, return the indices


       mp = {}
       for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
            return [mp[diff], i]
        mp[num] = i
        
        
            



        