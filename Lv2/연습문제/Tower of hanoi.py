def solution(n):
    answer = []
    
    def hanoi(x, y, z, n):
        if n == 1:
            answer.append([x, z])
            return
        hanoi(x, z, y, n - 1)
        hanoi(x, y, z, 1)
        hanoi(y, x, z, n - 1)
    
    hanoi(1, 2, 3, n)
    
    return answer
