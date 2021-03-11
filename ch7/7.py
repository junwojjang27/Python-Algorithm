def twoSum(nums, target):
    cnt = 0
    cnt_2 = 0
    for num in nums:
        for num_2 in nums:
            if cnt_2 != cnt:
                if target == num + num_2:
                    return cnt, cnt_2
            cnt_2 += 1
        cnt += 1
        cnt_2 = 0

                


if __name__ == '__main__':
    nums = [-3, 4, 3, 90]
    target = 0
    print(twoSum(nums, target))

"""
더욱 효율적인 방법이 7(answer).py 에 저장
"""