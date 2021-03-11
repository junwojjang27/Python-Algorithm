def arrayPairSum(nums):
    nums.sort()
    sum = 0
    for i in range (0, len(nums), 2):
        sum += nums[i]
    return sum


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))


"""
파이썬의 장점을 활용해 한줄로 만드는 법

return sum(sorted(nums))

"""