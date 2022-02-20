# Create a program prints out how many indicies it took to sum the target value. 
# We have to assume that there is only one solution and not use the same element twice
#  Example 
# Input nums = [1, 7, 2, 8], target = 3
# Output = [0,2]
# Exp: nums[0] + nums[2] == 3

# Edge Cases
    # What if we have multiple numbers leading to the same summation ? 
    #  nums = [1, 2, 1, 2] target = 3

    # What if that value is already available as it is ?
    # nums = [0, 1, 3, 4] target = 1
    # Here output could be just nums[1] or should we take nums[0] + nums[1]

# Breaking down the problem
# If we want to get all the index whose value would sum to the target, the brute force way would be to sum each combination and check if the pair or multiple pairs correspond to the value
# That would increase the complexitiy and other factors of the solution 

# One of the things that can be done is only consider elements which is smaller than the sum 
# We would create a for loop for the sum that is iterating over the selected values
# sum value is getting added and the value index is appended into  a new list
# if the sum value is found the appened list is given out as output

# Pseudo Code
# nums = entry list
# target = goal value
# sum = 0
# outlist = []
# while(sum != target):
#     for values in nums:
#         if values < target:
#             sum = sum + values
#             outlist.append(index(values))


from operator import index
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is a brute force solution
        # for iNumber in range(len(nums)):
        #     if nums[iNumber] <= target:
        #         for jNumber in range(iNumber+1, len(nums)):
        #                 if nums[iNumber] + nums[jNumber] == target:
        #                     return[iNumber, jNumber]

        # This is the best solution using hashmap
        hashmap = {}
        for (i, n) in enumerate(nums):
            diff = target - n
            print(diff, target, n)
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

        

s = Solution()

s.twoSum([1, 2, 1, 2], 3)
