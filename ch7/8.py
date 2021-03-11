def trap(height):
    
    if len(height)==0:
        return 0

    temp = max(height)

    cnt=0
    for i in height:
        if i == temp:
            break
        cnt+=1

    left, right = cnt-1, cnt+1

    answer = 0

    while left > 0:
        temp_2 = max(height[:left+1])
        while True:
            if height[left] == temp_2:
                temp = temp_2
                left -= 1
                break
            else:
                answer += temp_2-height[left]
                left -= 1

    while right < len(height):
        temp_2 = max(height[right:])
        while True:
            if height[right] == temp_2:
                temp = temp_2
                right += 1
                break
            else:
                answer += temp_2-height[right]
                right += 1
    
    return answer




if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))