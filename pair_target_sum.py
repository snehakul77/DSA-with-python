#Given an array of integers and a target , find out of there's a pair that adds up to the target.
#This logic will be applicable only if the array is an sorted array
#over here logic works like first the 2 pointers will be assigned the values, the an current sum is created
#with addition of lower index value and higher index value. if current sum value is lesser that target value then increase the left index,
#if current sum is greater that the target value then decrease the right index.
#arr =[1, 2, 4, 4] , target = 8

def has_pair(arr, k):
    left = 0
    right = len(arr) - 1
    while left < right:
        cuurent_sum = arr[left] + arr[right]
        if cuurent_sum == k:
            return True
        elif cuurent_sum < k:
            left +=1
        else:
            right -=1
    return False

print(has_pair([1, 2, 4, 4],8))




