def solution(n):
    answer = 0
    # 연속한 자연수
    # 1. 자연수 1부터 + 2, 3, 증가시키면서 되면 stop
    cnt = 0
    val = n
    total = 0
    for i in range(1, n + 1):
        total = 0
        for j in range(i, n + 1):
            total = total + j
            if(total == val):
                cnt += 1
                break
            elif total > n:
                break

    return cnt
