class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:return -1 
        else:return nums.index(target)
        

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
