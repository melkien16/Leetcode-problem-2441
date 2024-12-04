def numbers(nums):
    largest = -1
    for i in nums:
        if i > 0 and -i in nums and i > largest:
            largest = i
    return largest



nums = [-10,8,6,7,-2,-3]


print(numbers(nums))