
def solution(s):
    answer_list = []
    answer=''
    
    for i in s:
        if i==' ':
            answer_list.append(answer.capitalize())
            answer_list.append(' ')
            answer=''
        else:
            answer+=i
    answer_list.append(answer.capitalize())
    return ''.join(answer_list)

# 공백인 경우도 추가