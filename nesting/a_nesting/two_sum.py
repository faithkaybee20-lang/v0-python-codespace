([2, 3, 5, 9], 7) 
([2, 3, 5, 9], 4) 
([6, 3, 4], 10) 
([6, 5, 1], 10) 

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
