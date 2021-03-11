def threeSum(nums):
    nums.sort()
    
    sum = 0

    zero = []
    check = 0

    left, right = 1, len(nums)-1

    for i in range (len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        
        for j in range (len(nums)-(i+2)):
            if check == 1:
                if nums[left] == nums[left+1]:
                    check = 1
                    left += 1
                else:
                    check = 0
                    left +=1
                continue
            if check == 2:
                if nums[right] == nums[right-1]:
                    check = 2
                    right -= 1
                else:
                    check = 0
                    right -= 1
                continue

            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                zero.append([nums[i], nums[left], nums[right]])
                if nums[left] == nums[left+1]:
                    check = 1
                left += 1
            elif sum > 0:
                if nums[right] == nums[right-1]:
                    check = 2
                right -= 1
            else:
                if nums[left] == nums[left+1]:
                    check = 1
                left += 1
                
        check = 0
    return zero


if __name__ == '__main__':
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(threeSum(nums))

"""
중간 식이 지저분하지만 큰 알고리즘은 맞았음.
"""