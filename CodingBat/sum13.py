"""
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""

nums = [13, 13]


def sum13(nums):
    result = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] == 13:
            result -= nums[i]
            try:
                if nums[i+1] != 13:
                    result -= nums[i+1]
            except IndexError:
                if nums[-1] == 13:
                    result
                result -= 0
        result += nums[i]
    return result


print(sum13(nums))
