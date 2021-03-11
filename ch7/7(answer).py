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


"""
딕셔너리에 값과 인덱스를 뒤집어서 저장한 뒤
target - num 인 값을 찾아 value로 인덱스를 알아내서
리턴하는 방법
"""