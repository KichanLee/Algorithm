def solution(priorities, location):

    answer = [-1]*len(priorities)

    cnt = 1
    len_ = len(priorities)
    ind = 0
    while answer[location] == -1:

        if priorities[ind] == max(priorities):
            answer[ind] = cnt
            cnt += 1
            priorities[ind] = -1

        ind += 1
        ind %= len_


    return answer[location]
