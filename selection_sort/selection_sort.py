def selection_sort(nums):

    for i in range(5):
        minpos= i
        quit
        for j in range(i,6):
            if nums[j] <nums[minpos]:
                minpos = j
        
        temp =nums[i]
        nums[i] = nums[minpos]
        nums[minpos]= temp

        print(nums)
    return nums

nums =[5,3,8,6,7,2]
selection_sort(nums)
print(nums)
# Output: [2, 3, 5, 6, 7,8]
# The selection sort algorithm sorts the list in ascending order.






