"""

TASK 2. A list containing 1-n items is given. Write a function that will check what elements are missing:

1-n = [1,2,3,4,5,...,10]
for example: n=10
input: [2,3,7,4,9], 10
output: [1,5,6,8,10]

"""


def get_missing_elements(nums, n):
    result = [i for i in range(1, n+1)]
    for num in nums:
        if num in result:
            result.remove(num)
    return result
