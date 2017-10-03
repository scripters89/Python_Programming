"""
Created on Tue Apr 11 09:30:03 2017

@author: mashiksa
"""
#Selection Sort
def selsort(nums):
    len1 = len(nums)
    for i in range(len1):
        min1 = i
        for j in range(min1,len1):
            if nums[j] < nums[min1]:
                nums[j], nums[min1] = nums[min1], nums[j]
    return nums

#Customized      
def selsort_op(nums):
    len1 = len(nums)
    edge = len1-1
    for i in range(len1):
        min1 = i
        for j in range(min1,edge):
            if nums[j] < nums[min1]:
                nums[j], nums[min1] = nums[min1], nums[j]
            if nums[j] > nums[edge]:
                nums[j], nums[edge] = nums[edge], nums[j]
        edge -= 1
    return nums
