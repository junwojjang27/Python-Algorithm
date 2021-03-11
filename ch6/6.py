def longestPalindrome(s):

        cnt_list = []

        #문자열 첫번째부터 팰린드롬이 이뤄지는 자릿수 구하기
        for i in range(len(s)): 

            left = i-1
            right = i+1

            cnt = 1

            while left>=0 or right<=(len(s)-1):
                if right>(len(s)-1):
                    if s[left] == s[i]:
                        cnt += 1
                        left -=1
                    else:
                        break
                elif left<0:
                    if s[right] == s[i]:
                        cnt += 1
                        right +=1
                    else:
                        break
                else:
                    if s[i] == s[left] and s[i] == s[right]:
                        cnt += 2
                        left -= 1
                        right += 1
                    elif s[left] == s[i]:
                        cnt += 1
                        left -=1
                    elif s[right] == s[i]:
                        cnt += 1
                        right +=1
                    else:
                        break


            while left>=0 and right<=(len(s)-1):
                if s[left] == s[right]:
                    cnt += 2
                    left -= 1
                    right += 1
                else:
                    break

            cnt_list.append(cnt)    #순서대로 팰린드롬 자릿수 저장

        answer_index = 0

        for i in range(len(cnt_list)-1):    #가장 긴 팰린드롬 자릿수
            if cnt_list[i] == max(cnt_list):
                answer_index = i
                break

        answer = s[answer_index]

        cnt_2 = 1

        left = answer_index-1
        right = answer_index+1

        while cnt_2 < max(cnt_list):    #가장 긴 팰린드롬 출력
            if left>=0 and right<=(len(s)-1):
                if s[left] == s[right]:
                    answer = s[left] + answer + s[right]
                    left -= 1
                    right += 1
                    cnt_2 += 2
                else:
                    if s[left] == s[right-1]:
                        answer = s[left] + answer
                        left -= 1
                        cnt_2 +=1
                    else:
                        answer = answer + s[right]
                        right += 1
                        cnt_2 += 1
            elif left<0:
                answer = answer + s[right]
                right += 1
                cnt_2 += 1
            else:
                answer = s[left] + answer
                left -= 1
                cnt_2 += 1

        return answer

if __name__ == '__main__':
    s = "abbcccbbbcaaccbababcbcabca"

    print(longestPalindrome(s))


"""
내가 한 방법과 같이 하나씩 비교하는 것보다
두개, 세개 씩 비교한 뒤 팰린드롬일 경우 앞 뒤로 하나씩 추가하는 방법이
훨씬 빠르고 간편하다.
두개짜리 세개짜리 나눠서 하는 이유는 가운데가 짝수의 같은 문자일 경우가 있기 때문
ex) abccba 일 경우 세개짜리 로는 팰린드롬임을 알 수 없다.

나는 가장 긴 팰린드롬의 자릿수를 구한 뒤, 그 자릿수를 가진 팰린드롬을 만들어나갔는데
max()를 이용하여 매우 간편하게 구현할 수 있다.
ex) result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    위 코드를 설명하면, 없을경우(''), 두칸짜리, 세칸짜리, 자릿수
"""