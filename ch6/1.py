def isPalindrome(s):

    str_chg = ''

    for a in s:       #영어, 한글, 숫자만 남기기
        if a.isalnum() == True:
            str_chg += a

    str_chg = str_chg.lower()   #모든 영어를 소문자로 변환

    if str_chg == str_chg[::-1]:    #팰린드롬 판별
        return True
    else:
        return False

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))


"""
re.sub('패턴', 교체함수, '문자열', 바꿀회수) 를 사용해서
더욱 빠르고 간편하게 구현 가능
ex) str = re.sub('[^a-z0-9]', '', str)
"""