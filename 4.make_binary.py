def convert_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def count_zeros(s):
    count = 0
    i = 0
    while i < len(s):
        if s[i] == '0':
            count += 1
        i += 1
    return count

def solution(s):
    conversion_count = 0
    removed_zeros = 0
    
    while s != '1':
        removed_zeros += count_zeros(s)
        
        new_len = len(s) - count_zeros(s) # python  에는 s.count('0') 하면 찾아준대..
        
        s = convert_binary(new_len) # python 은 내장함수로 bin(new_len)[2:] 하면 이진법 변환해줌
                                    # 2번째 자리부터 슬라이싱하는 이유는 앞에 0b가 붙기때문
        
        conversion_count += 1
    
    return [conversion_count, removed_zeros]
