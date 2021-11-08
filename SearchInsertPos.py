nums = [1,3,5,6]
target = 2
l,u = 0,len(nums)-1
while l<=u:
    mid = (l+u)//2
    print("mid")
    # 1 
    print(mid)
    # 0 0 
    # 1 >= 2 
    if nums[mid] >= target:
        # 3 >= 2
        # u = 0
        u = mid-1
        print("u")
        print(u)
    else:
    #   l = 0 = 1 
        l = mid+1
        print("lo")
        print(l)

 
print("op")
print(l)


'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0

'''
