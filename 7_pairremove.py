def solution(s):
    
    stack = []

    for i in s:
        if stack: # stack not null
            if(i == stack[len(stack) -1]): # i == stack[-1]
                stack.pop()
                continue
            else:
                stack.append(i)
        else:     # stack null
            stack.append(i)
            
    if not stack:
        return 1

    return 0
