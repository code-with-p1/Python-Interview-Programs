class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for key, val in enumerate(nums):
            if key < (len(nums)-1):
                sum = nums[key] + nums[key+1]
                if sum == target:
                    result.clear()
                    result.extend([key, key+1])
        return result
    
result = Solution()
result = result.twoSum([2,7,11,15], 9)
print(result)

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
