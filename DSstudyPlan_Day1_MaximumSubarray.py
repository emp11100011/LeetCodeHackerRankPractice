class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        '''
        Initial Solution
        maxSum = []
        for i in range(len(nums)):
            sumStack = []
            for j in range(i+1, len(nums)+1):
                sumStack.append(sum(nums[i:j]))
            maxSum.append(max(sumStack))
        return max(maxSum)
        '''
        # Kadane's Algorithm
        currentSubArray = maxSub = nums[0]
        for num in nums[1:]:
            currentSubArray = max(num, currentSubArray + num)
            maxSub = max(maxSub, currentSubArray)
        return maxSub

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])