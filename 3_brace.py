def solution(s):
    answer = True
    
    # s를 stack에 하나씩 넣는다.
    # stack에 넣고 )를 만나면 pop하고 pop해서 ( 이면 pass
    stack = []
    for brace in s:
        if(brace == '('):
            stack.append('(')
        elif(brace == ')'):
            if (not stack):
                return False
            elif(stack.pop() != '('):
                return False
    # 비어있는지도 확인
    if stack :
        return False
    return True