def findDuplicate(nums):
    slow,fast,finder=nums[0],nums[nums[0]],0
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    while True:
        slow = nums[slow]
        finder = nums[finder]
        
        if slow == finder:
            return slow

nums = [1,4,3,2,2]

print(findDuplicate(nums))