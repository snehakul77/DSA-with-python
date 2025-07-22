#Given height[]. an array of non negative integers where each value represents the height of a vertical lineon the x axis , find the 2 lines
#lines that together with the x axis for a container such that the container holds the most water.

def max_area(height):
    left,right = 0,len(height) -1
    max_water = 0
    while left < right:
        width = right -left
        water = min(height[left], height[right]) * width
        max_water = max(max_water, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1,8,6,2,5,4,8,3,7]))
