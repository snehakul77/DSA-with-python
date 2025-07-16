#Rotate the array to the right by k steps
#This is using in place rotation

def reverse_subarray(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

def rotate_array_inplace(arr,k):
    n = len(arr)
    k = k % n

    reverse_subarray(arr,0,n-1)
    reverse_subarray(arr,0,k-1)
    reverse_subarray(arr,k,n-1)
    return arr

arr = [1,2,3,4,5]
k = 3
print(rotate_array_inplace(arr,k))