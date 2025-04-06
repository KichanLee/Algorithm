def solution(clothes):
    answer = 0
 
    clothes_dict = {
      cloth[1] : 0 for cloth in clothes
    }

    
    for cloth in clothes:
        clothes_dict[cloth[1]] += 1

    
    temp = 1
    for num in clothes_dict.values():
        temp = temp * (num + 1)

    answer = temp - 1

    return answer

