def solution(numbers, direction):
    k = -1 if direction == "right" else 1
    answer = [numbers[(i + k) % len(numbers)] for i in range(0, len(numbers))]
    
    return answer
