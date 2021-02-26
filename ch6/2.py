def reverseString(s):
    str_list = s    #리스트 형식으로 만들기

    left = 0
    right = len(str_list)-1

    while left < right:     #리스트 조작
        temp = str_list[left]
        str_list[left] = str_list[right]
        str_list[right] = temp
        left+=1
        right-=1

if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)




"""
left값과 right값을 서로 바꿀 때 temp를 이용 할 필요 없이
str_list[left], str_list[right] = str_list[right], str_list[left]
위와 같이 한번에 가능.

위 방법과 같이 포인터를 이용하지 않고 리스트에서만 제공하는
reverse() 함수를 사용하여 즉시 뒤집을 수 있음.
ex) str_list.reverse()
"""