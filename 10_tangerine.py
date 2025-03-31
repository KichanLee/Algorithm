from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)  

    answer = 0
    total = 0 

    for c in sorted_counts:
        total += c
        answer += 1
        if total >= k:
            break

    return answer
