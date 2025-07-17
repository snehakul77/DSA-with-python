#Given an sorted array , remove the duplicates in place so that each element appears only once and return the length of the unique part
#Here use 2 variables or the pointers, one will be the slow pointer to track the start and other one will be the look pointer to compare with the previous one.
#Will start by assiging one pointer to 0 and will loop the rest of array with another pointer.

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i +=1
            nums[i] = nums[j]
    return i + 1

arr = [1, 1, 2, 2, 3]
length = remove_duplicates(arr)
print("Unique part : ", arr[:length])
print("Length :", length)