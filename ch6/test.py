def twoSum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[num] = i
    for i, num in enumerate(nums):
        if target - num in nums_dict and i != nums_dict[target - num]:
            return nums.index(num), nums_dict[target-num]

                


if __name__ == '__main__':
    nums = [-3, 4, 3, 90]
    target = 0
    print(twoSum(nums, target))

