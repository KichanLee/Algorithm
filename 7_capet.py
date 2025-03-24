def solution(brown, yellow):
    total = brown + yellow
    
    # w >= h
    for w in range(1, total + 1):   # 1, total + 1 까지 range돌면서
        if total % w == 0:          # 12 % 1 == 0:
            h = total // w          # 12 =  12 // 1
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w, h]
