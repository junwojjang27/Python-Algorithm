import re

def mostCommonWord(paragraph, banned):

    paragraph = paragraph.lower()   #모든 영어를 소문자로 바꿈.

    paragraph = re.sub('[^a-z]', ' ', paragraph)    #영어 소문자만 남기기.

    list_p = paragraph.split()     #단어별로 리스트에 저장
    dict_p = {}

    for p in list_p:        #딕셔너리에 단어, 빈도수 저장
        if p not in banned:
            if p in dict_p:
                dict_p[p] += 1
            else:
                dict_p[p] = 1

    max = 0
    max_word = ''
    for k, v in dict_p.items():     #가장 빈도수 높은 단어 구함
        if v > max:
            max = v
            max_word = k

    return max_word

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(mostCommonWord(paragraph, banned))