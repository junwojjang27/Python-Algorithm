def reorderLogFiles(logs):
        
    num, char = [], []

    for log in logs:        # 문자로그, 숫자로그 나누기
        if log.split()[1].isdigit():
            num.append(log)
        else:
            char.append(log)

    char.sort(key = lambda x : (x.split()[1:], x.split()[0]))
    #문자로그를 정렬, 기준은 식별자 제외후 정렬하고 같다면 식별자 순으로.

    return char + num

if __name__ == '__main__':
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    print(reorderLogFiles(logs))

"""
답안을 보고 작성함
split()과 lambda 표현식 제대로 이해하기

람다 표현식
: 식별자 없이 실행 가능한 함수를 말하며 함수 선언 없이도
하나의 식으로 함수를 단순하게 표현할 수 있다.
"""