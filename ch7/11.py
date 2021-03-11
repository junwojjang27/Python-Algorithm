def productExceptSelf(nums):
    left = []
    right = []

    mul = 1
    for num in nums[:(len(nums)-1)]:
        mul *= num
        left.append(mul)

    mul = 1
    for i in range(len(nums)-1):
        mul *= nums[-1-i]
        right.append(mul)

    answer = []

    for i in range(len(nums)):
        if i == 0:
            answer.append(right[-1])
        elif i == len(nums)-1:
            answer.append(left[-1])
        else:
            mul = 1
            mul = left[i-1] * right[-i-1]
            answer.append(mul)
        
    return answer

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))

"""
left, right를 모두 구한뒤에 answer을 구하는 것보다
left만 구해놓고 right를 찾음과 동시에 answer을 구하는 것이 더 효과적이다.
"""