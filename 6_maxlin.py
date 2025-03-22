def solution(s):
    
    
    answer = s.split(' ')
    
    min_num = min(map(int, answer))
    max_num = max(map(int, answer))
    
    word = str(min_num) + ' ' + str(max_num)
    # word = f"{str(min_num)} {str(max_num)}"
        
    return word
