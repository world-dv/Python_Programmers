def solution(numbers):
    answer = []
    
    for i, j in enumerate(numbers):
        for a, b in enumerate(numbers):
            if i != a:
                c = j + b
                if c not in answer:
                    answer.append(c)
    return sorted(answer)
