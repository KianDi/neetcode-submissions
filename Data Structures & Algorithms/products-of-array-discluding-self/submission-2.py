class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## naive approach:
        ## calculate the product of every number
        ## then divide by the number at current indice

        ## more optimized output could is multiplying everything before
        ## and after a certain indices
        ## how to do this?

        # build suffix array
        # prefix[i] = product of all elements before index i

        result = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(0, len(nums)):
            result[i] = prefix[i] * suffix[i] 
        return result

