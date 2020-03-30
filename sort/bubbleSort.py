"""
冒泡排序
冒泡排序是由两层循环套起来的，看循环，先找到最内层，从内层往外看。
"""


def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


nums = [5, 3, 28, 79, 33, 2, 1]

print(bubbleSort(nums))
