"""
    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        
        index_map = {}  # Dictionary to store the number and its index

        # Loop through the list of numbers
        for i, v in enumerate(nums):
 
            complement = target - v
            
            # If the complement is already in the dictionary, return the indices
            if complement in index_map:
                return [index_map[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            index_map[v] = i

        # If no solution is found (though per the problem statement, one always exists)
        return None





# Instantiate the Solution class
obj = Solution()

# Define nums and target
nums = [2, 11, 7, 15]
target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,3]
# target = 6

# Call the twoSum method
result = obj.twoSum(nums, target)

# Print the result
print(result)  





