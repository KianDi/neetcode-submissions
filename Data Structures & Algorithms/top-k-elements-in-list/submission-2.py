class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we want to return the k most frequent elements in the array nums
        # first thought-
        # create hash map to store frequency of each number
        # key = value of num, value = freq of number
        # built a list of frequency, number pairs from map
        # sort this list by frequency. 
        # initialize empty result array
        # pop from array, add to rsult array until k is reached
        # this will take O(nlogn) because we are using the sort function.


        # optimized route
        # We intialize an array of size n + 1 which will contain following:
        # key: freq, value: num values corresponding
        # we assign numbers to the key that corresponds with their frequency, which
        # can be done by creating an array of pairs with frequency and value to fill
        # the map
        # then we iterate in reverse of the map, extracting values until we hit k numbers in
        # our result array

        n = len(nums)
        freq_array = [[] for _ in range(n+1)]
        count = {}
        result = []
        max_k = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # count
        # key: actual num, value: actual freq
        for key, value in count.items():
            freq_array[value].append(key)
        for i in range(n, 0, -1):
            for num in freq_array[i]:
                result.append(num)
                if len(result) == k:
                    return result

        # O(n) time and space
            

        