def solution(A,B):
    answer = 0
    
    size = len(A)
    A.sort()
    B.sort(reverse=True)

    
    for i in range(size):
        answer += A[i] * B[i]
        
    
    # 1. 길이 구하기
    # 2. 최솟값 최대값 곱해서 저장하기
    # 3. 해당 인덱스 끝내기
#     size = len(A)ㄴ
    
#     for i in range(size):
#         a_min = min(A)
#         b_max = max(B)
#         A.remove(a_min)
#         B.remove(b_max)
#         answer += a_min * b_max
#          이렇게 풀면 시간복잡도 초과 n2
#           정렬 후에 하면 시간복잡도 nlogn이 나옴
#        python sort함수의 시간복잡도는 최악의 경우도 nlogn임.
        
    return answer