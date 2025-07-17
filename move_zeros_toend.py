#Given an array of integers , move all 0s to end while maintaining the relative order og the non zero element.
#Using 2 pointers technique

def move_zeros_toend(nums):
    non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i],nums[non_zero]
            non_zero += 1
    return nums

arr = [0, 1, 0, 3, 12]
print(move_zeros_toend(arr))